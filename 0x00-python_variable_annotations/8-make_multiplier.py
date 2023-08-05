#!/usr/bin/env python3
"""
This script defines a function to create a multiplier function.

Author: Myles181
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier factor.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the specified multiplier.

        Args:
            x (float): The input float value.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier
    return multiplier_function
