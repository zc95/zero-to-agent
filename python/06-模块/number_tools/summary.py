"""Summarize a series imported from the same package."""

from .series import fib2


def fib_sum(limit):
    """Return the sum of Fibonacci numbers below limit."""
    return sum(fib2(limit))
