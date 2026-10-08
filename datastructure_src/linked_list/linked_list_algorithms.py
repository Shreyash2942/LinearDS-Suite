"""Example algorithms that use the custom LinkedList class."""

from collections.abc import Iterable
from typing import Any

from .linked_list import LinkedList


def manage_tasks(
    tasks: Iterable[Any], task_to_remove: Any, task_to_find: Any
) -> dict[str, Any]:
    """Build a task list, remove one matching task, and search the result.

    Return the initial and updated display strings, whether removal succeeded,
    and whether the searched task remains. Preserve input order and leave the
    input collection unchanged. Task values are stored, not executed.
    """
    task_list = LinkedList()
    for task in tasks:
        task_list.insert(task)

    initial_sequence = task_list.display()
    removed = task_list.delete(task_to_remove)
    found = task_list.search(task_to_find)

    return {
        "initial_sequence": initial_sequence,
        "removed": removed,
        "found": found,
        "updated_sequence": task_list.display(),
    }
