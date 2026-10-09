"""A list-backed queue with first-in, first-out ordering."""

from typing import Any


class Queue:
    """Store items in FIFO order, with the front at index zero."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self._items: list[Any] = []

    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the front item; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.pop(0)

    def front(self) -> Any:
        """Return the front item without removing it; raise IndexError if empty."""
        if self.isEmpty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self._items[0]

    def isEmpty(self) -> bool:
        """Return whether the queue contains no items."""
        return not self._items

    def to_list(self) -> list[Any]:
        """Return a shallow snapshot in front-to-rear order."""
        return self._items.copy()
