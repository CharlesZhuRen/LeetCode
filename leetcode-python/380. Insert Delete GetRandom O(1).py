class RandomizedSet:

    def __init__(self):
        self.nums = []  # 一个list存储数值
        self.indices = {}  # 一个哈希表存储位置

    def insert(self, val: int) -> bool:
        if val in self.indices:  # 判断键是否存在 这个操作在字典里确实是o1时间复杂度
            return False

        self.indices[val] = len(self.nums)  # 更新索引=原数组长度
        self.nums.append(val)  # 拓展数组
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:  # 判断键是否存在
            return False
        id = self.indices[val]  # 从哈希表中取得索引

        self.nums[id] = self.nums[-1]  # 用数组中最后一个数赋值给要删除的数
        self.indices[self.nums[id]] = id  # 更新被保留的原来的最后那个数的索引
        self.nums.pop()  # 删除数组中最后一个数, 不立即删除是因为这一步会改变数组长度
        del self.indices[val]  # 在哈希表中删除这个键值对

        return True

    def getRandom(self) -> int:
        from random import choice
        return choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
