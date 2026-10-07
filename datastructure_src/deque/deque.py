"""A list-backed deque supporting insertion and removal at both ends."""

from typing import Any


class Deque:
    """Store items with the front at index zero and the rear at the end."""

    def __init__(self) -> None:
        """Create an empty deque."""
        self._items: list[Any] = []

    def addFront(self, item: Any) -> None:
        """Add an item to the front of the deque."""
        self._items.insert(0, item)

    def addRear(self, item: Any) -> None:
        """Add an item to the rear of the deque."""
        self._items.append(item)

    def removeFront(self) -> Any:
        """Remove and return the front item; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot remove from the front of an empty deque.")
        return self._items.pop(0)

    def removeRear(self) -> Any:
        """Remove and return the rear item; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot remove from the rear of an empty deque.")
        return self._items.pop()

    def isEmpty(self) -> bool:
        """Return whether the deque contains no items."""
        return not self._items
