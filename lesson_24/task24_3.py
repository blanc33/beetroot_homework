from typing import Optional
def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers
    mult(2, 4) == 8
    True
    mult(2, 0) == 0
    True
    mult(2, -4)
    ValueError("This function works only with postive integers")
    """
    if n < 0:
        raise ValueError("This function works only with postive integers")
    elif n == 0:
        return 0
    elif n == 1:
        return a
    else:
        return a+mult(a, n-1)

print(mult(2, 4))

