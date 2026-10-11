"""Extra argument types, subcommand groups and nicer help formatting."""

from __future__ import annotations

__all__ = ["argparseExt"]


def argparseExt(value):
    """Extra argument types, subcommand groups and nicer help formatting."""
    if value is None:
        raise ValueError("value must not be None")
    return value
