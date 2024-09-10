class MyHashSet:

    def __init__(self):
        self.length = 257
        self.nums = [None] * self.length

    def add(self, key: int) -> None:
        index = hash(key) % self.length
        if self.nums[index] == None:
            self.nums[index] = [key]
        else:
            if key not in self.nums[index]:
                self.nums[index].append(key)

    def remove(self, key: int) -> None:
        index = hash(key) % self.length
        if self.nums[index] is not None and key in self.nums[index]:
            self.nums[index].remove(key)

    def contains(self, key: int) -> bool:
        index = hash(key) % self.length
        if self.nums[index] is None:
            return False
        else:
            return key in self.nums[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
