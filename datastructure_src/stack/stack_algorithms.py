"""Example algorithms that use the custom Stack class."""

from .stack import Stack


def is_balanced_parentheses(expression: str) -> bool:
    """Check that (), [], and {} match and nest correctly.

    Ignore non-bracket characters. Empty input is balanced. This checks
    bracket structure only; it does not parse quoted strings or comments.
    """
    stack = Stack()
    matching_openers = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.push(character)
        elif character in matching_openers:
            if stack.isEmpty() or stack.pop() != matching_openers[character]:
                return False

    return stack.isEmpty()
