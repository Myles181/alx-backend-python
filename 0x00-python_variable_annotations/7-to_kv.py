#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a string and the square of a given int/float value.

    Args:
        k (str): The string value.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the input string and the square of v as a float.
    """
    return (k, v * v)
