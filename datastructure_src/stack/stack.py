"""A list-backed stack with last-in, first-out ordering."""

from typing import Any


class Stack:
    """Store items in LIFO order using an internal Python list."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top item without removing it; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._items[-1]

    def isEmpty(self) -> bool:
        """Return whether the stack contains no items."""
        return not self._items

    def to_list(self) -> list[Any]:
        """Return a shallow snapshot in bottom-to-top order."""
        return self._items.copy()
