from typing import Sequence, Union, Any

# The types of the elements of the input are not know
# {'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
def safe_first_element(lst: Sequence[Any])->Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
