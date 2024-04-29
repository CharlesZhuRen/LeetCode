import random


class randomized_set:
    def __init__(self):
        self.values = []
        self.val_to_index = {}
        self.length = 0

    def insert(self, val):
        if val in self.val_to_index:
            return False

        self.values.append(val)
        self.val_to_index[val] = self.length
        self.length += 1
        return True

    def remove(self, val):
        if val not in self.val_to_index:
            return False

        # 把最后一个值移动和被删除的值互换位置，然后删除最后一个值也就是删除了要被删除的那个值
        idx = self.val_to_index[val]
        last_value = self.values[-1]
        self.values[idx] = last_value
        self.val_to_index[last_value] = idx
        del self.val_to_index[val]  # self.val_to_index.pop(val) 效果一样，但del更通用，删除什么都可以
        self.values.pop()
        return True

    def getRandom(self):
        return random.choice(self.values)


if __name__ == '__main__':
    rs = randomized_set()
    print(rs.values)
    print(rs.insert(1))
    print(rs.values)
    print(rs.insert(2))
    print(rs.values)
    print(rs.insert(1))
    print(rs.values)
    print(rs.remove(1))
    print(rs.values)
    print(rs.remove(1))
    print(rs.values)
    print(rs.insert(3))
    print(rs.values)

    print(rs.getRandom())
    print(rs.getRandom())
