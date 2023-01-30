class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


def reverse(string):
    n = len(string)
    stack = Stack()
    for i in range(0, n):
        stack.push(string[i])

    string = ""

    for i in range(0, n):
        string += stack.pop()

    return string


string = "Stack"
string = reverse(string)
print("Reversed string is " + string)