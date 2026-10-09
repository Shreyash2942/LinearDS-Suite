"""A singly linked list built from Node objects."""

from typing import Any

from .node import Node


class LinkedList:
    """Manage an ordered chain of nodes through an internal head reference."""

    def __init__(self) -> None:
        """Create an empty linked list."""
        self._head: Node | None = None

    def insert(self, data: Any) -> None:
        """Append a new node containing data to the end of the list."""
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            return

        current = self._head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, data: Any) -> bool:
        """Remove the first equal value; return False if no match exists."""
        previous = None
        current = self._head

        while current is not None:
            if current.data == data:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def search(self, data: Any) -> bool:
        """Return whether a node contains a value equal to data."""
        current = self._head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self) -> str:
        """Return the node values separated by arrows and ending with None."""
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        return " -> ".join(values)

    def to_list(self) -> list[Any]:
        """Return a shallow snapshot of node values in list order."""
        values = []
        current = self._head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values
