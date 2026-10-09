"""Exercise real Streamlit widgets, navigation, state, and error messages."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from datastructure_src.deque import Deque
from datastructure_src.linked_list import LinkedList
from datastructure_src.queue import Queue
from datastructure_src.stack import Stack

APP_PATH = Path(__file__).resolve().parents[1] / "streamlit_app" / "app.py"


@pytest.fixture
def app():
    return AppTest.from_file(str(APP_PATH), default_timeout=15).run()


def open_page(app, name):
    app.switch_page(f"pages/{name}_page.py").run()
    assert not app.exception


def click(app, key):
    app.button(key).click().run()
    assert not app.exception


def enter_value(app, input_key, value, button_key):
    app.text_input(input_key).set_value(value)
    click(app, button_key)


def test_home_initializes_actual_structure_objects(app):
    assert not app.exception
    assert isinstance(app.session_state.stack, Stack)
    assert isinstance(app.session_state.queue, Queue)
    assert isinstance(app.session_state.deque, Deque)
    assert isinstance(app.session_state.linked_list, LinkedList)
    assert any(title.value == "LinearDS-Suite" for title in app.title)


@pytest.mark.parametrize("name", ["stack", "queue", "deque", "linked_list", "algorithms"])
def test_each_page_loads(app, name):
    open_page(app, name)


def test_stack_controls_follow_lifo_and_peek_preserves_values(app):
    open_page(app, "stack")
    enter_value(app, "stack_value", "first", "stack_push")
    enter_value(app, "stack_value", "second", "stack_push")
    assert app.session_state.stack.to_list() == ["first", "second"]
    assert app.code[0].value.index("second") < app.code[0].value.index("first")

    click(app, "stack_peek")
    assert app.success[0].value == "Top item: 'second'."
    assert app.session_state.stack.to_list() == ["first", "second"]
    click(app, "stack_pop")
    assert app.success[0].value == "Removed 'second'."
    assert app.session_state.stack.to_list() == ["first"]


def test_queue_controls_follow_fifo_and_front_preserves_values(app):
    open_page(app, "queue")
    enter_value(app, "queue_value", "first", "queue_enqueue")
    enter_value(app, "queue_value", "second", "queue_enqueue")
    click(app, "queue_front")
    assert app.success[0].value == "Front item: 'first'."
    assert app.session_state.queue.to_list() == ["first", "second"]
    click(app, "queue_dequeue")
    assert app.success[0].value == "Removed 'first'."
    assert app.session_state.queue.to_list() == ["second"]


def test_deque_controls_operate_on_both_ends(app):
    open_page(app, "deque")
    enter_value(app, "deque_value", "middle", "deque_add_rear")
    enter_value(app, "deque_value", "front", "deque_add_front")
    enter_value(app, "deque_value", "rear", "deque_add_rear")
    assert app.session_state.deque.to_list() == ["front", "middle", "rear"]
    click(app, "deque_remove_front")
    assert app.session_state.deque.to_list() == ["middle", "rear"]
    click(app, "deque_remove_rear")
    assert app.session_state.deque.to_list() == ["middle"]


def test_linked_list_controls_insert_search_delete_and_display(app):
    open_page(app, "linked_list")
    for value in ("first", "second", "first"):
        enter_value(app, "linked_list_value", value, "linked_list_insert")
    click(app, "linked_list_search")
    assert app.success[0].value == "Found 'first'."
    click(app, "linked_list_delete")
    assert app.session_state.linked_list.to_list() == ["second", "first"]
    click(app, "linked_list_display")
    assert app.code[0].value == "second -> first -> None"
    enter_value(app, "linked_list_value", "missing", "linked_list_delete")
    assert "not found" in app.warning[0].value
    assert app.session_state.linked_list.to_list() == ["second", "first"]
    click(app, "linked_list_search")
    assert "not found" in app.info[0].value


@pytest.mark.parametrize(
    ("page", "button"),
    [
        ("stack", "stack_pop"), ("stack", "stack_peek"),
        ("queue", "queue_dequeue"), ("queue", "queue_front"),
        ("deque", "deque_remove_front"), ("deque", "deque_remove_rear"),
    ],
)
def test_empty_operations_show_errors_without_crashing(app, page, button):
    open_page(app, page)
    click(app, button)
    assert "empty" in app.error[0].value
    assert app.session_state[page].to_list() == []


@pytest.mark.parametrize(
    ("page", "button"),
    [("stack", "stack_push"), ("queue", "queue_enqueue"),
     ("deque", "deque_add_front"), ("deque", "deque_add_rear"),
     ("linked_list", "linked_list_insert")],
)
def test_blank_values_are_rejected(app, page, button):
    open_page(app, page)
    enter_value(app, f"{page}_value", "   ", button)
    assert app.error
    assert app.session_state[page].to_list() == []


@pytest.mark.parametrize("button", ["linked_list_delete", "linked_list_search"])
def test_blank_linked_list_queries_show_errors(app, button):
    open_page(app, "linked_list")
    click(app, button)
    assert app.error


@pytest.mark.parametrize(
    ("page", "add", "clear"),
    [("stack", "stack_push", "stack_clear"),
     ("queue", "queue_enqueue", "queue_clear"),
     ("deque", "deque_add_rear", "deque_clear"),
     ("linked_list", "linked_list_insert", "linked_list_clear")],
)
def test_state_survives_page_switching_and_clear_affects_only_one_structure(app, page, add, clear):
    open_page(app, page)
    enter_value(app, f"{page}_value", "retained", add)
    original_object = app.session_state[page]
    other_page = "queue" if page != "queue" else "stack"
    other_structure = app.session_state[other_page]
    open_page(app, other_page)
    open_page(app, page)
    assert app.session_state[page] is original_object
    assert original_object.to_list() == ["retained"]
    click(app, clear)
    assert app.session_state[page].to_list() == []
    assert app.session_state[other_page] is other_structure
    assert app.metric[0].value == "0"


@pytest.mark.parametrize(
    ("page", "add"),
    [("stack", "stack_push"), ("queue", "queue_enqueue"), ("deque", "deque_add_rear")],
)
def test_is_empty_control_uses_current_state(app, page, add):
    open_page(app, page)
    click(app, f"{page}_empty")
    assert app.info[0].value == f"The {page} is empty."
    enter_value(app, f"{page}_value", "value", add)
    click(app, f"{page}_empty")
    assert app.info[0].value == f"The {page} is not empty."


def test_user_sessions_have_independent_objects(app):
    other_app = AppTest.from_file(str(APP_PATH), default_timeout=15).run()
    assert not other_app.exception
    app.session_state.stack.push("only in first session")
    assert other_app.session_state.stack.to_list() == []


def test_bracket_example_handles_valid_invalid_and_empty_input(app):
    open_page(app, "stack")
    click(app, "stack_demo_run")
    assert app.success[0].value == "Balanced"
    enter_value(app, "stack_demo_expression", "([)]", "stack_demo_run")
    assert "Not balanced" in app.warning[0].value
    enter_value(app, "stack_demo_expression", "", "stack_demo_run")
    assert app.success[0].value == "Balanced"


def test_processing_example_preserves_fifo_and_handles_blank_lines(app):
    open_page(app, "queue")
    app.text_area("queue_demo_tasks").set_value(" Task A \n\nTask B\nTask C")
    click(app, "queue_demo_run")
    assert app.code[0].value == "Task A → Task B → Task C"
    app.text_area("queue_demo_tasks").set_value(" \n")
    click(app, "queue_demo_run")
    assert any("No tasks" in info.value for info in app.info)


def test_palindrome_example_matches_exact_characters(app):
    open_page(app, "deque")
    click(app, "deque_demo_run")
    assert app.success[0].value == "Palindrome"
    enter_value(app, "deque_demo_text", "Racecar", "deque_demo_run")
    assert app.warning[0].value == "Not a palindrome"
    enter_value(app, "deque_demo_text", "", "deque_demo_run")
    assert app.success[0].value == "Palindrome"


def test_management_example_displays_updates_and_missing_task_results(app):
    open_page(app, "linked_list")
    click(app, "linked_list_demo_run")
    assert app.code[-1].value == "Task A -> Task C -> None"
    assert any("Removed" in message.value for message in app.success)
    assert any("Found" in message.value for message in app.success)
    enter_value(app, "linked_list_demo_remove", "missing", "linked_list_demo_run")
    assert "not found" in app.warning[0].value
    assert app.code[-1].value == "Task A -> Task B -> Task C -> None"
    enter_value(app, "linked_list_demo_find", "missing", "linked_list_demo_run")
    assert any("not found" in message.value for message in app.info)
    enter_value(app, "linked_list_demo_remove", " ", "linked_list_demo_run")
    assert app.error


@pytest.mark.parametrize(
    "example",
    ["Balanced parentheses · Stack", "Task processing · Queue",
     "Palindrome checker · Deque", "Dynamic tasks · Linked List"],
)
def test_algorithm_hub_runs_each_example_without_modifying_interactive_objects(app, example):
    app.session_state.stack.push("stack value")
    app.session_state.queue.enqueue("queue value")
    app.session_state.deque.addRear("deque value")
    app.session_state.linked_list.insert("list value")
    before = {key: app.session_state[key].to_list() for key in ("stack", "queue", "deque", "linked_list")}
    open_page(app, "algorithms")
    app.selectbox("algorithm_example").select(example).run()
    click(app, "algorithms_demo_run")
    assert app.success
    for key, values in before.items():
        assert app.session_state[key].to_list() == values
