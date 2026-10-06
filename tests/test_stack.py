"""Verify the Stack API and balanced-parentheses algorithm."""

import pytest

from datastructure_src.stack import Stack, is_balanced_parentheses


def test_new_stack_is_empty():
    assert Stack().isEmpty() is True


def test_push_adds_item_to_top():
    stack = Stack()

    assert stack.push(10) is None
    assert stack.isEmpty() is False
    assert stack.peek() == 10


def test_pop_follows_lifo_order():
    stack = Stack()
    for item in (10, 20, 30):
        stack.push(item)

    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.isEmpty() is True


def test_peek_does_not_remove_top_item():
    stack = Stack()
    stack.push("bottom")
    stack.push("top")

    assert stack.peek() == "top"
    assert stack.peek() == "top"
    assert stack.pop() == "top"
    assert stack.pop() == "bottom"
    assert stack.isEmpty() is True


@pytest.mark.parametrize("operation", ["pop", "peek"])
def test_empty_operation_raises_index_error(operation):
    stack = Stack()

    with pytest.raises(IndexError, match="empty stack"):
        getattr(stack, operation)()

    assert stack.isEmpty() is True
    stack.push("usable after error")
    assert stack.pop() == "usable after error"


def test_stack_instances_have_independent_storage():
    first = Stack()
    second = Stack()
    first.push("first only")

    assert second.isEmpty() is True
    second.push("second only")
    assert first.pop() == "first only"
    assert second.pop() == "second only"


def test_stack_preserves_duplicates_and_arbitrary_objects():
    stack = Stack()
    payload = {"task": "review"}
    for item in (None, "duplicate", "duplicate", payload):
        stack.push(item)

    assert stack.peek() is payload
    assert stack.pop() is payload
    assert stack.pop() == "duplicate"
    assert stack.pop() == "duplicate"
    assert stack.pop() is None
    assert stack.isEmpty() is True


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("", True),
        ("plain text", True),
        (" \t\n", True),
        ("()", True),
        ("[]", True),
        ("{}", True),
        ("{[()]}", True),
        ("()[]{}", True),
        ("((()))", True),
        ("([{}])", True),
        ("(a + b) * [c - {d / e}]", True),
        ("(", False),
        ("[", False),
        ("{", False),
        (")", False),
        ("]", False),
        ("}", False),
        ("(]", False),
        ("([)]", False),
        ("{[(])}", False),
        ("(()", False),
        ("())", False),
        (")(", False),
        ("valid () then [", False),
    ],
)
def test_balanced_parentheses(expression, expected):
    assert is_balanced_parentheses(expression) is expected


def test_parentheses_checks_do_not_share_stack_state():
    assert is_balanced_parentheses("(") is False
    assert is_balanced_parentheses("{[()]}") is True
    assert is_balanced_parentheses(")") is False
    assert is_balanced_parentheses("") is True
