#!/usr/bin/env python3
"""
This script defines a function to calculate the sum of elements in a list of floats.

Author: Myles181
"""

def sum_list(input_list: list[float]) -> float:
    """
    Calculate the sum of elements in a list of floats.

    Args:
        input_list (list[float]): A list containing float elements.

    Returns:
        float: The sum of elements in the input list.
    """
    total_sum = 0.0
    for i in input_list:
        total_sum += i
    return total_sum