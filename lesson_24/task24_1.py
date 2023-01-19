from typing import Optional, Union

def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    """
    Returns  x ^ exp

    to_power(2, 3) == 8
    True

    to_power(3.5, 2) == 12.25
    True

    to_power(2, -1)
    ValueError: This function works only with exp > 0.
    """
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    elif exp == 0:
        return 1
    elif exp == 1:
        return x
    else:
        return x * to_power(x, exp-1)

print(to_power(2, 3))