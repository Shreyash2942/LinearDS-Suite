"""Verify that visualization snapshots preserve order and protect storage."""

import pytest

from datastructure_src.deque import Deque
from datastructure_src.linked_list import LinkedList
from datastructure_src.queue import Queue
from datastructure_src.stack import Stack


@pytest.mark.parametrize(
    ("factory", "addition", "removal"),
    [
        (Stack, "push", "pop"),
        (Queue, "enqueue", "dequeue"),
        (Deque, "addRear", "removeFront"),
        (LinkedList, "insert", "delete"),
    ],
)
def test_snapshot_preserves_order_and_cannot_modify_storage(factory, addition, removal):
    structure = factory()
    assert structure.to_list() == []
    payload = {"task": "review"}
    for value in (None, "same", "same", payload):
        getattr(structure, addition)(value)

    snapshot = structure.to_list()
    assert snapshot == [None, "same", "same", payload]
    assert snapshot[-1] is payload
    snapshot.clear()
    assert structure.to_list() == [None, "same", "same", payload]

    earlier_snapshot = structure.to_list()
    if isinstance(structure, LinkedList):
        structure.delete(None)
    else:
        getattr(structure, removal)()
    assert earlier_snapshot == [None, "same", "same", payload]
    assert len(structure.to_list()) == 3
