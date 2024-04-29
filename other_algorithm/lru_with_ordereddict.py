from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            # 更新这个key在所有key中的顺序，也就是把它移动到最后
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        if key in self.cache:  # 如果key已经存在，移动到最后
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:  # 如果容量已满，把last used踢出
            self.cache.popitem(last=False)
        # 更新 or 添加kv
        self.cache[key] = value

    def __str__(self):
        res = []

        for k, v in self.cache.items():
            res.append((k, v))

        return res.__str__()


if __name__ == '__main__':
    lru_cache = LRUCache(capacity=3)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    print(lru_cache)

    lru_cache.put(4, 4)
    print(lru_cache)
    lru_cache.get(2)
    print(lru_cache)
    lru_cache.put(5, 5)
    print(lru_cache)