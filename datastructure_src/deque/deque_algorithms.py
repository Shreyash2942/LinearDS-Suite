"""Example algorithms that use the custom Deque class."""

from .deque import Deque


def is_palindrome(text: str) -> bool:
    """Check whether text reads identically from both ends.

    Compare characters exactly, including case, spaces, and punctuation.
    Empty text and single characters are palindromes.
    """
    deque = Deque()
    for character in text:
        deque.addRear(character)

    while not deque.isEmpty():
        front = deque.removeFront()
        if deque.isEmpty():
            return True
        if front != deque.removeRear():
            return False

    return True
