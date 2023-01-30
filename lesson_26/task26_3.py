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


    def get_from_stack(self, el):

        stack2 = Stack()
        while self.peek() != el:
            stack2.push(self.pop())
            if self.size() == 0:
                raise ValueError("Element not found!")
        else:
            self.pop()
        while stack2.size() != 0:
            self.push(stack2.pop())
        return self

stack = Stack()
stack.push("i")
stack.push("a")
stack.push("s")
stack.push("f")
stack.push("g")
stack.push("j")
stack.push("k")
print(stack)
print(stack.get_from_stack("s"))


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, el):
        queue2 = Queue()
        length = self.size()
        while self.size() != 0:
            q = self.dequeue()
            if q == el:
                pass
            else:
                queue2.enqueue(q)
        if length == queue2.size():
            raise ValueError("Element not found!")
        while queue2.size() != 0:
            self.enqueue(queue2.dequeue())
        return self


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    q.enqueue('cat')
    q.enqueue('tiger')
    q.enqueue('lion')
    q.enqueue('mouse')
    print(q)
    q.get_from_stack("cat")
    print(q)

