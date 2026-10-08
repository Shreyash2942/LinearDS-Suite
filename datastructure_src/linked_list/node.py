"""A node for a singly linked list."""

from __future__ import annotations

from typing import Any


class Node:
    """Store a value and a reference to the next node."""

    def __init__(self, data: Any) -> None:
        """Create a node whose next reference is initially None."""
        self.data = data
        self.next: Node | None = None
