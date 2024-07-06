class List:
    def __init__(self):
        self._capacity: int = 10
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> int:
        if index >= self._size or index < 0:
            raise IndexError("out of size")
        return self._arr[index]

    def set(self, num: int, index: int):
        if index >= self._size or index < 0:
            raise IndexError("out of size")
        self._arr[index] = num

    def add(self, num: int) -> int:
        if self._size == self._capacity:
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int) -> int:
        if index >= self._size or index < 0:
            raise IndexError("out of size")
        if self._size == self._capacity:
            self.extend_capacity()
        for i in range(self._size - 1, index - 1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[index] = num
        self._size += 1

    def remove_by_index(self, index: int) -> int:
        if index >= self._size or index < 0:
            raise IndexError("out of size")
        num = self._arr[index]
        for i in range(index, self._size - 1):
            self._arr[i] = self._arr[i + 1]
        self._size -= 1
        return num

    def extend_capacity(self) -> int:
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio - 1)
        self._capacity = self.capacity() * self._extend_ratio

    def to_array(self) -> list[int]:
        return self._arr[:self._size]

    def to_info(self) -> str:
        return "capacity = {}, size = {}, extend_ratio = {}\n{}"\
            .format(self._capacity, self._size, self._extend_ratio, str(self.to_array()))


if __name__ == '__main__':
   alist = List()
   alist.add(1)
   alist.add(2)
   alist.add(3)
   print(alist.to_info())
   alist.remove_by_index(0)
   print(alist.to_info())

