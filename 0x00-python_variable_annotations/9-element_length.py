!/usr/bin/env python3
"""
This script defines a function to calculate the lengths of sequences in an iterable.

Author: Myles181
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the lengths of sequences in an iterable.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]