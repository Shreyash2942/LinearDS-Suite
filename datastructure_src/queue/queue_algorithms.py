"""Example algorithms that use the custom Queue class."""

from collections.abc import Iterable
from typing import Any

from .queue import Queue


def process_tasks(tasks: Iterable[Any]) -> list[Any]:
    """Simulate FIFO service and return tasks in their processing order.

    Enqueue all incoming tasks, then service them one at a time. Task values
    are returned unchanged; this simulation does not execute task payloads.
    An empty input returns an empty list.
    """
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)

    processed_tasks = []
    while not queue.isEmpty():
        processed_tasks.append(queue.dequeue())

    return processed_tasks
