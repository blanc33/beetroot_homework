def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    is_palindrome('mom')
    True

    is_palindrome('sassas')
    True

    is_palindrome('o')
    True
    """

    if index <= len(looking_str) // 2:
        if looking_str[index] == looking_str[len(looking_str)-index-1]:
            return is_palindrome(looking_str, index+1)
        else:
            return False
    else:
        return True

print(is_palindrome('m'))