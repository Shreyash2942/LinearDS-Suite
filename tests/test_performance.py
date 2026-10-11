"""Verify benchmark state reset, saved measurements, and CLI behavior."""

from dataclasses import replace
import json
from pathlib import Path
import subprocess
import sys

import pytest

from datastructure_src.queue import Queue
from performance.benchmark import CASES, load_results, measure_case, run_benchmarks


def test_small_benchmark_records_all_cases_and_round_trips_saved_results(tmp_path):
    data = run_benchmarks(sizes=[3, 5], repeats=2, search_probes=4)
    assert len(data["results"]) == 2 * len(CASES)
    assert data["metadata"]["setup_timed"] is False
    for record in data["results"]:
        assert len(record["samples_seconds"]) == 2
        assert all(sample >= 0 for sample in record["samples_seconds"])
        assert record["best_seconds"] == min(record["samples_seconds"])
        expected_count = 4 if record["scenario"] == "search_last" else 1 if record["scenario"] == "delete_last" else record["n"]
        assert record["operations_per_trial"] == expected_count
        assert record["microseconds_per_operation"] == pytest.approx(record["best_seconds"] * 1_000_000 / expected_count)
    destination = tmp_path / "results.json"
    destination.write_text(json.dumps(data), encoding="utf-8")
    assert load_results(destination) == data


def test_destructive_benchmark_rebuilds_state_before_each_trial():
    lengths = []

    class ObservedQueue(Queue):
        def dequeue(self):
            lengths.append(len(self.to_list()))
            return super().dequeue()

    case = next(case for case in CASES if case.operation == "dequeue")
    measure_case(replace(case, factory=ObservedQueue), n=3, repeats=3, search_probes=2)
    assert lengths == [3, 2, 1] * 4  # One warm-up plus three timed trials.


@pytest.mark.parametrize(
    "options",
    [{"sizes": []}, {"sizes": [0]}, {"sizes": [2, 2]}, {"repeats": 0}, {"search_probes": 0}],
)
def test_benchmark_rejects_invalid_parameters(options):
    with pytest.raises(ValueError):
        run_benchmarks(**options)


def test_saved_results_missing_or_malformed_are_reported(tmp_path):
    destination = tmp_path / "results.json"
    with pytest.raises(FileNotFoundError):
        load_results(destination)
    destination.write_text("{broken JSON", encoding="utf-8")
    with pytest.raises(ValueError):
        load_results(destination)
    destination.write_text('{"schema_version": 99, "results": []}', encoding="utf-8")
    with pytest.raises(ValueError):
        load_results(destination)


def test_command_line_writes_results(tmp_path):
    destination = tmp_path / "results.json"
    project_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(project_root / "performance" / "benchmark.py"), "--sizes", "2", "--repeats", "1",
         "--search-probes", "2", "--output", str(destination)],
        cwd=tmp_path, capture_output=True, text=True, check=True,
    )
    assert "Saved 11 measurements" in result.stdout
    assert load_results(destination)["metadata"]["sizes"] == [2]
    assert "datastructure_src/linked_list/linked_list.py" in load_results(destination)["metadata"]["implementation_sha256"]
