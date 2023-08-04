from typing import Mapping, Any, Union, TypeVar

# Define a type variable ~T
T = TypeVar('~T')

# Define the function with type annotations
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
