"""Verify Node, LinkedList, and dynamic task management."""

import pytest

from datastructure_src.linked_list import LinkedList, Node, manage_tasks


@pytest.mark.parametrize("data", [10, "task", None, [], {"task": "review"}])
def test_node_stores_data_and_starts_without_a_next_node(data):
    node = Node(data)

    assert node.data is data
    assert node.next is None


def test_node_can_reference_another_node():
    first = Node("first")
    second = Node("second")
    first.next = second

    assert first.next is second
    assert first.next.data == "second"
    assert second.next is None


def test_new_linked_list_is_empty():
    linked_list = LinkedList()

    assert linked_list.display() == "None"
    assert linked_list.search("missing") is False
    assert linked_list.delete("missing") is False
    assert linked_list.display() == "None"


def test_first_insert_works():
    linked_list = LinkedList()

    assert linked_list.insert(10) is None
    assert linked_list.display() == "10 -> None"
    assert linked_list.search(10) is True


def test_multiple_inserts_preserve_order():
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.insert(value)

    assert linked_list.display() == "10 -> 20 -> 30 -> None"


@pytest.mark.parametrize("value", [10, 20, 30])
def test_search_finds_values_at_each_position(value):
    linked_list = LinkedList()
    for item in (10, 20, 30):
        linked_list.insert(item)

    assert linked_list.search(value) is True
    assert linked_list.display() == "10 -> 20 -> 30 -> None"


def test_search_returns_false_for_missing_value():
    linked_list = LinkedList()
    linked_list.insert("present")

    assert linked_list.search("missing") is False
    assert linked_list.display() == "present -> None"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (10, "20 -> 30 -> None"),
        (20, "10 -> 30 -> None"),
        (30, "10 -> 20 -> None"),
    ],
    ids=["head", "middle", "last"],
)
def test_delete_removes_matching_node_at_each_position(value, expected):
    linked_list = LinkedList()
    for item in (10, 20, 30):
        linked_list.insert(item)

    assert linked_list.delete(value) is True
    assert linked_list.search(value) is False
    assert linked_list.display() == expected


def test_delete_missing_value_leaves_list_unchanged():
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.insert(value)

    assert linked_list.delete(99) is False
    assert linked_list.display() == "10 -> 20 -> 30 -> None"


def test_delete_only_node_then_reuse_list():
    linked_list = LinkedList()
    linked_list.insert("only")

    assert linked_list.delete("only") is True
    assert linked_list.display() == "None"
    assert linked_list.delete("only") is False
    linked_list.insert("new")
    assert linked_list.display() == "new -> None"


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (["same", "middle", "same"], "middle -> same -> None"),
        (["start", "same", "middle", "same"], "start -> middle -> same -> None"),
        (["same", "same"], "same -> None"),
    ],
)
def test_delete_removes_only_first_matching_value(values, expected):
    linked_list = LinkedList()
    for value in values:
        linked_list.insert(value)

    assert linked_list.delete("same") is True
    assert linked_list.display() == expected
    assert linked_list.search("same") is True


def test_insert_after_deleting_last_node_preserves_order():
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.insert(value)

    assert linked_list.delete(30) is True
    linked_list.insert(40)
    assert linked_list.display() == "10 -> 20 -> 40 -> None"


def test_remove_all_nodes_then_insert_again():
    linked_list = LinkedList()
    for value in (10, 20, 30):
        linked_list.insert(value)
    for value in (20, 30, 10):
        assert linked_list.delete(value) is True

    assert linked_list.display() == "None"
    linked_list.insert(40)
    linked_list.insert(50)
    assert linked_list.display() == "40 -> 50 -> None"


def test_linked_list_instances_have_independent_storage():
    first = LinkedList()
    second = LinkedList()
    first.insert("first only")

    assert second.display() == "None"
    second.insert("second only")
    assert first.display() == "first only -> None"
    assert second.display() == "second only -> None"
    assert first.delete("first only") is True
    assert second.search("second only") is True


def test_none_and_falsy_values_are_valid_data():
    linked_list = LinkedList()
    for value in (None, 0, ""):
        linked_list.insert(value)

    assert linked_list.display() == "None -> 0 ->  -> None"
    assert linked_list.search(None) is True
    assert linked_list.delete(None) is True
    assert linked_list.search(None) is False
    assert linked_list.search(0) is True
    assert linked_list.search("") is True


def test_search_and_delete_use_value_equality():
    linked_list = LinkedList()
    linked_list.insert({"task": "review"})
    linked_list.insert({"task": "submit"})

    assert linked_list.search({"task": "review"}) is True
    assert linked_list.delete({"task": "review"}) is True
    assert linked_list.display() == "{'task': 'submit'} -> None"


def test_display_returns_string_without_printing_or_changing_list(capsys):
    linked_list = LinkedList()
    linked_list.insert("Task A")
    linked_list.insert("Task B")

    assert linked_list.display() == "Task A -> Task B -> None"
    assert linked_list.display() == "Task A -> Task B -> None"
    assert capsys.readouterr().out == ""
    assert linked_list.search("Task A") is True
    assert linked_list.search("Task B") is True


def test_manage_tasks_adds_removes_searches_and_displays():
    tasks = ["Task A", "Task B", "Task C"]

    result = manage_tasks(tasks, "Task B", "Task C")

    assert result == {
        "initial_sequence": "Task A -> Task B -> Task C -> None",
        "removed": True,
        "found": True,
        "updated_sequence": "Task A -> Task C -> None",
    }
    assert tasks == ["Task A", "Task B", "Task C"]


def test_manage_tasks_handles_empty_input():
    assert manage_tasks([], "missing", "missing") == {
        "initial_sequence": "None",
        "removed": False,
        "found": False,
        "updated_sequence": "None",
    }


def test_manage_tasks_handles_missing_values():
    assert manage_tasks(["Task A"], "missing", "missing") == {
        "initial_sequence": "Task A -> None",
        "removed": False,
        "found": False,
        "updated_sequence": "Task A -> None",
    }


@pytest.mark.parametrize(
    ("tasks", "expected_found", "expected_sequence"),
    [
        (["Task A"], False, "None"),
        (["Task A", "Task A"], True, "Task A -> None"),
    ],
)
def test_manage_tasks_searches_after_removing_first_match(
    tasks, expected_found, expected_sequence
):
    result = manage_tasks(tasks, "Task A", "Task A")

    assert result["removed"] is True
    assert result["found"] is expected_found
    assert result["updated_sequence"] == expected_sequence


def test_manage_tasks_accepts_a_generator():
    tasks = (f"Task {letter}" for letter in "ABC")

    result = manage_tasks(tasks, "Task A", "Task C")

    assert result["initial_sequence"] == "Task A -> Task B -> Task C -> None"
    assert result["removed"] is True
    assert result["found"] is True
    assert result["updated_sequence"] == "Task B -> Task C -> None"


def test_manage_tasks_supports_none_as_a_value():
    assert manage_tasks([None, "Task A"], None, "Task A") == {
        "initial_sequence": "None -> Task A -> None",
        "removed": True,
        "found": True,
        "updated_sequence": "Task A -> None",
    }


def test_task_management_examples_do_not_share_state():
    assert manage_tasks(["Task A", "Task B"], "Task A", "Task B")["found"] is True
    assert manage_tasks([], "Task B", "Task B")["found"] is False
