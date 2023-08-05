from typing import Union

def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    Calculate the sum of elements in a mixed list of integers and floats.

    Args:
        mxd_lst (Union[int, float]): A mixed list containing integers and/or floats.

    Returns:
        float: The sum of elements in the mixed list.
    """
    sum_result = 0.0
    for i in mxd_lst:
        sum_result += i
    return sum_result