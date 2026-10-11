"""Measure custom structures with timeit and save results for the UI."""

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import timeit
from typing import Any, Callable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from datastructure_src.deque import Deque
from datastructure_src.linked_list import LinkedList
from datastructure_src.queue import Queue
from datastructure_src.stack import Stack

RESULTS_PATH = Path(__file__).with_name("results.json")


@dataclass(frozen=True)
class BenchmarkCase:
    """Describe one timed workload and its input preparation."""

    structure: str
    operation: str
    factory: Callable[[], Any]
    fill_method: str
    mode: str
    operation_complexity: str
    trial_complexity: str


CASES = (
    BenchmarkCase("Stack", "push", Stack, "push", "add", "O(1) amortized", "O(n)"),
    BenchmarkCase("Stack", "pop", Stack, "push", "drain", "O(1) amortized", "O(n)"),
    BenchmarkCase("Queue", "enqueue", Queue, "enqueue", "add", "O(1) amortized", "O(n)"),
    BenchmarkCase("Queue", "dequeue", Queue, "enqueue", "drain", "O(n) worst case", "O(n^2)"),
    BenchmarkCase("Deque", "addFront", Deque, "addRear", "add", "O(n) worst case", "O(n^2)"),
    BenchmarkCase("Deque", "addRear", Deque, "addRear", "add", "O(1) amortized", "O(n)"),
    BenchmarkCase("Deque", "removeFront", Deque, "addRear", "drain", "O(n) worst case", "O(n^2)"),
    BenchmarkCase("Deque", "removeRear", Deque, "addRear", "drain", "O(1) amortized", "O(n)"),
    BenchmarkCase("LinkedList", "insert", LinkedList, "insert", "add", "O(n) worst case", "O(n^2)"),
    BenchmarkCase("LinkedList", "search", LinkedList, "insert", "search_last", "O(n) worst case", "O(p*n)"),
    BenchmarkCase("LinkedList", "delete", LinkedList, "insert", "delete_last", "O(n) worst case", "O(n)"),
)


def measure_case(case: BenchmarkCase, n: int, repeats: int, search_probes: int) -> dict:
    """Measure fresh trials with setup outside each timed interval."""
    structure = None

    def prepare():
        nonlocal structure
        structure = case.factory()
        if case.mode != "add":
            fill = getattr(structure, case.fill_method)
            for value in range(n):
                fill(value)

    def workload():
        operation = getattr(structure, case.operation)
        if case.mode == "add":
            for value in range(n):
                operation(value)
        elif case.mode == "drain":
            for _ in range(n):
                operation()
        elif case.mode == "search_last":
            for _ in range(search_probes):
                operation(n - 1)
        else:
            operation(n - 1)

    timer = timeit.Timer(workload, setup=prepare)
    timer.timeit(number=1)  # Untallied warm-up; subsequent trials rebuild state.
    samples = timer.repeat(repeat=repeats, number=1)
    count = search_probes if case.mode == "search_last" else 1 if case.mode == "delete_last" else n
    best = min(samples)
    return {
        "structure": case.structure,
        "operation": case.operation,
        "scenario": case.mode,
        "n": n,
        "operations_per_trial": count,
        "operation_complexity": case.operation_complexity,
        "trial_complexity": case.trial_complexity,
        "samples_seconds": samples,
        "best_seconds": best,
        "microseconds_per_operation": best * 1_000_000 / count,
    }


def implementation_hashes() -> dict[str, str]:
    """Record which source files produced a benchmark snapshot."""
    paths = [Path(__file__).relative_to(PROJECT_ROOT)]
    paths.extend(path.relative_to(PROJECT_ROOT)
                 for path in (PROJECT_ROOT / "datastructure_src").rglob("*.py"))
    return {path.as_posix(): hashlib.sha256((PROJECT_ROOT / path).read_bytes()).hexdigest()
            for path in sorted(paths)}


def run_benchmarks(sizes=(100, 1_000, 10_000), repeats=5, search_probes=100) -> dict:
    """Benchmark all cases using positive input sizes and repetition counts."""
    sizes = list(sizes)
    if not sizes or any(n < 1 for n in sizes) or repeats < 1 or search_probes < 1:
        raise ValueError("Sizes, repeats, and search probes must all be positive.")
    if len(sizes) != len(set(sizes)):
        raise ValueError("Input sizes must be unique.")
    records = [measure_case(case, n, repeats, search_probes)
               for n in sorted(sizes) for case in CASES]
    return {
        "schema_version": 1,
        "metadata": {
            "created_at_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "sizes": sorted(sizes),
            "repeats": repeats,
            "search_probes": search_probes,
            "statistic": "minimum of repeated full trials",
            "timer": "timeit default_timer (perf_counter)",
            "setup_timed": False,
            "warmup_trials": 1,
            "garbage_collection": "disabled by timeit during each trial",
            "implementation_sha256": implementation_hashes(),
        },
        "results": records,
    }


def load_results(path: Path | None = None) -> dict:
    """Read saved measurements; reject incomplete or invalid result records."""
    with (path or RESULTS_PATH).open(encoding="utf-8") as source:
        data = json.load(source)
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Unsupported or empty benchmark results.")
    metadata = data.get("metadata")
    records = data.get("results")
    if not isinstance(metadata, dict) or not isinstance(records, list) or not records:
        raise ValueError("Benchmark metadata and result records are required.")
    for key in ("python", "platform", "created_at_utc", "repeats", "search_probes", "sizes"):
        metadata[key]
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each benchmark record must be an object.")
        for key in ("structure", "operation", "scenario", "trial_complexity"):
            record[key]
        for key in ("n", "operations_per_trial", "best_seconds", "microseconds_per_operation"):
            value = record[key]
            if not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError(f"Invalid benchmark value: {key}.")
        if record["n"] < 1 or record["operations_per_trial"] < 1:
            raise ValueError("Benchmark sizes and operation counts must be positive.")
    return data


def main() -> None:
    """Run the command-line benchmark and write the measured JSON snapshot."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", nargs="+", type=int, default=[100, 1_000, 10_000])
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--search-probes", type=int, default=100)
    parser.add_argument("--output", type=Path, default=RESULTS_PATH)
    args = parser.parse_args()
    try:
        data = run_benchmarks(args.sizes, args.repeats, args.search_probes)
    except ValueError as error:
        parser.error(str(error))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("Structure   Operation       n     Trial (ms)   Average/op (us)")
    for row in data["results"]:
        print(f"{row['structure']:<11} {row['operation']:<12} {row['n']:>6} "
              f"{row['best_seconds'] * 1_000:>12.6f} {row['microseconds_per_operation']:>17.6f}")
    print(f"Saved {len(data['results'])} measurements to {args.output}")


if __name__ == "__main__":
    main()
