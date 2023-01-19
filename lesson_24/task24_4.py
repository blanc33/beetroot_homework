def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    reverse("hello") == "olleh"
    True
    reverse("o") == "o"
    True
    """
    if len(input_str) == 0:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]


reverseme = 'Desserts'
print(reverse(reverseme))