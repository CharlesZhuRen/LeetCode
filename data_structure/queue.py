# 在一端进行插入, 在另一端进行删除

class Queue(object):
    """队列"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列, 即始终在下标为0的位置插入新元素"""
        self.items.insert(0, item)

    def dequeue(self):
        """
        出队列, 即始终pop最后一个元素
        当然也可以append+pop(0), 到底哪一端进哪一端出并不重要
        """
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
