class ListNode:
    def __init__(self, _val=0, _next=None):
        self._val: int = _val
        self._next = _next

    def get_val(self) -> int:
        return self._val

    def get_next(self):
        return self._next


class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, val: int):
        node = ListNode(val)
        node._next = self._peek
        self._peek = node
        self._size += 1

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("empty stack")
        return self._peek.get_val()

    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.get_next()
        self._size -= 1
        return num

    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.get_val())
            node = node.get_next()
        arr.reverse()
        return arr