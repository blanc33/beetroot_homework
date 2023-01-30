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


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(myStr):
    stack = Stack()
    for i in myStr:
        if i in open_list:
            stack.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((stack.size() > 0) and
                    (open_list[pos] == stack.peek())):
                stack.pop()
            else:
                return "Unbalanced"
    if stack.size() == 0:
        return "Balanced"
    else:
        return "Unbalanced"


string = "{[]{()}}"
print(string, "-", check(string))

string = "[{}{})(]"
print(string, "-", check(string))

string = "((()"
print(string, "-", check(string))