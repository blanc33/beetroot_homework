def sum_of_digits(digit_string: str) -> int:
    """
    sum_of_digits('26') == 8
    True
    sum_of_digits('test')
    ValueError("input string must be digit string")
    """
    try:
        if len(digit_string) == 1:
            return int(digit_string)
        else:
            return int(digit_string[0]) + sum_of_digits(digit_string[1:])
    except ValueError:
        return ValueError("input string must be digit string")

print(sum_of_digits('test'))
