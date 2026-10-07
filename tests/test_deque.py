"""Verify the Deque API and palindrome checker."""

import pytest

from datastructure_src.deque import Deque, is_palindrome


def test_new_deque_is_empty():
    assert Deque().isEmpty() is True


@pytest.mark.parametrize("operation", ["addFront", "addRear"])
def test_add_puts_item_in_deque(operation):
    deque = Deque()

    assert getattr(deque, operation)(10) is None
    assert deque.isEmpty() is False
    assert deque.removeFront() == 10
    assert deque.isEmpty() is True


@pytest.mark.parametrize(
    ("addition", "removal", "expected"),
    [
        ("addFront", "removeFront", [30, 20, 10]),
        ("addFront", "removeRear", [10, 20, 30]),
        ("addRear", "removeFront", [10, 20, 30]),
        ("addRear", "removeRear", [30, 20, 10]),
    ],
)
def test_order_is_preserved_at_both_ends(addition, removal, expected):
    deque = Deque()
    for item in (10, 20, 30):
        getattr(deque, addition)(item)

    assert [getattr(deque, removal)() for _ in expected] == expected
    assert deque.isEmpty() is True


def test_mixed_operations_at_both_ends():
    deque = Deque()
    deque.addRear("middle")
    deque.addFront("front")
    deque.addRear("rear")

    assert deque.removeFront() == "front"
    deque.addFront("new front")
    assert deque.removeRear() == "rear"
    deque.addRear("new rear")
    assert deque.removeFront() == "new front"
    assert deque.removeRear() == "new rear"
    assert deque.removeFront() == "middle"
    assert deque.isEmpty() is True


@pytest.mark.parametrize("addition", ["addFront", "addRear"])
@pytest.mark.parametrize("removal", ["removeFront", "removeRear"])
def test_single_item_can_be_removed_from_either_end(addition, removal):
    deque = Deque()
    getattr(deque, addition)("only item")

    assert getattr(deque, removal)() == "only item"
    assert deque.isEmpty() is True


@pytest.mark.parametrize("operation", ["removeFront", "removeRear"])
@pytest.mark.parametrize("previously_used", [False, True])
def test_empty_removal_raises_index_error(operation, previously_used):
    deque = Deque()
    if previously_used:
        deque.addRear("old item")
        deque.removeFront()

    with pytest.raises(IndexError, match="empty deque"):
        getattr(deque, operation)()

    assert deque.isEmpty() is True
    deque.addFront("new item")
    assert deque.removeRear() == "new item"


def test_deque_instances_have_independent_storage():
    first = Deque()
    second = Deque()
    first.addFront("first only")

    assert second.isEmpty() is True
    second.addRear("second only")
    assert first.removeRear() == "first only"
    assert second.removeFront() == "second only"


def test_deque_preserves_duplicates_and_arbitrary_objects():
    deque = Deque()
    payload = {"task": "review"}
    deque.addFront(None)
    deque.addRear("duplicate")
    deque.addRear("duplicate")
    deque.addRear(payload)

    assert deque.removeFront() is None
    assert deque.removeRear() is payload
    assert deque.removeFront() == "duplicate"
    assert deque.removeRear() == "duplicate"
    assert deque.isEmpty() is True


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", True),
        ("a", True),
        (" ", True),
        ("aa", True),
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("level", True),
        ("12321", True),
        ("a a", True),
        ("!a!", True),
        ("été", True),
        ("あいいあ", True),
        ("😀a😀", True),
        ("ab", False),
        ("abca", False),
        ("python", False),
        ("Racecar", False),
        ("aA", False),
        ("racecar ", False),
        ("racecar!", False),
        ("A man, a plan, a canal: Panama", False),
    ],
)
def test_palindrome_checker(text, expected):
    assert is_palindrome(text) is expected


def test_palindrome_checks_do_not_share_deque_state():
    assert is_palindrome("abca") is False
    assert is_palindrome("racecar") is True
    assert is_palindrome("") is True
