class Node(object):
    """节点"""

    def __init__(self, item):
        self._item = item
        self._next = None


class SinCycLinkedlist(object):
    """单向循环链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur._next != self._head:
            count += 1
            cur = cur._next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur._item)
        while cur._next != self._head:  # 判断是否到头
            cur = cur._next
            print(cur._item)
        print("")

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node._next = self._head
        else:
            # 添加的节点指向_head
            node._next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur._next != self._head:
                cur = cur._next
            cur._next = node
            # _head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node._next = self._head
        else:
            # 移到链表尾部
            cur = self._head
            while cur._next != self._head:
                cur = cur._next
            # 将尾节点指向node
            cur._next = node
            # 将node指向头节点_head
            node._next = self._head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur._next
            node._next = cur._next
            cur._next = node

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur._item == item:
            # 如果链表不止一个节点
            if cur._next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur._next != self._head:
                    cur = cur._next
                # cur指向了尾节点
                cur._next = self._head._next
                self._head = self._head._next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur._next != self._head:
                # 找到了要删除的元素
                if cur._item == item:
                    # 删除
                    pre._next = cur._next
                    return
                else:
                    pre = cur
                    cur = cur._next
            # cur 指向尾节点
            if cur._item == item:
                # 尾部删除
                pre._next = cur._next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur._item == item:
            return True
        while cur._next != self._head:
            cur = cur._next
            if cur._item == item:
                return True
        return False


if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
