"""Verify the Queue API and FIFO task-processing simulation."""

import pytest

from datastructure_src.queue import Queue, process_tasks


def test_new_queue_is_empty():
    assert Queue().isEmpty() is True


def test_enqueue_adds_item():
    queue = Queue()

    assert queue.enqueue("Task A") is None
    assert queue.isEmpty() is False
    assert queue.front() == "Task A"


def test_dequeue_follows_fifo_order():
    queue = Queue()
    for task in ("Task A", "Task B", "Task C"):
        queue.enqueue(task)

    assert queue.dequeue() == "Task A"
    assert queue.dequeue() == "Task B"
    assert queue.dequeue() == "Task C"
    assert queue.isEmpty() is True


def test_front_returns_first_item_without_removing_it():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.front() == 10
    assert queue.front() == 10
    assert queue.dequeue() == 10
    assert queue.front() == 20
    assert queue.dequeue() == 20
    assert queue.isEmpty() is True


@pytest.mark.parametrize("operation", ["dequeue", "front"])
@pytest.mark.parametrize("previously_used", [False, True])
def test_empty_operation_raises_index_error(operation, previously_used):
    queue = Queue()
    if previously_used:
        queue.enqueue("old task")
        queue.dequeue()

    with pytest.raises(IndexError, match="empty queue"):
        getattr(queue, operation)()

    assert queue.isEmpty() is True
    queue.enqueue("new task")
    assert queue.dequeue() == "new task"


def test_interleaved_operations_preserve_fifo_order():
    queue = Queue()
    queue.enqueue("Task A")
    queue.enqueue("Task B")
    assert queue.dequeue() == "Task A"
    queue.enqueue("Task C")

    assert queue.dequeue() == "Task B"
    assert queue.dequeue() == "Task C"
    assert queue.isEmpty() is True


def test_queue_instances_have_independent_storage():
    first = Queue()
    second = Queue()
    first.enqueue("first only")

    assert second.isEmpty() is True
    second.enqueue("second only")
    assert first.dequeue() == "first only"
    assert second.dequeue() == "second only"


def test_queue_preserves_duplicates_and_arbitrary_objects():
    queue = Queue()
    payload = {"task": "review"}
    for item in (None, "duplicate", "duplicate", payload):
        queue.enqueue(item)

    assert queue.front() is None
    assert queue.dequeue() is None
    assert queue.dequeue() == "duplicate"
    assert queue.dequeue() == "duplicate"
    assert queue.front() is payload
    assert queue.dequeue() is payload
    assert queue.isEmpty() is True


@pytest.mark.parametrize(
    "tasks",
    [[], ["Task A"], ["Task A", "Task B", "Task C"], [None, 0, "", "same", "same"]],
)
def test_process_tasks_returns_fifo_order_without_modifying_input(tasks):
    original = tasks.copy()

    result = process_tasks(tasks)

    assert result == original
    assert result is not tasks
    assert tasks == original


def test_process_tasks_accepts_a_generator():
    tasks = (f"Task {letter}" for letter in "ABC")

    assert process_tasks(tasks) == ["Task A", "Task B", "Task C"]


def test_process_tasks_preserves_object_identity():
    first = {"task": "review"}
    second = {"task": "submit"}

    result = process_tasks([first, second])

    assert result[0] is first
    assert result[1] is second


def test_processing_simulations_do_not_share_queue_state():
    assert process_tasks(["Task A", "Task B"]) == ["Task A", "Task B"]
    assert process_tasks([]) == []
    assert process_tasks(["Task C"]) == ["Task C"]
