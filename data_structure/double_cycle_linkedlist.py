class Node(object):
    """双向链表节点"""

    def __init__(self, item):
        self._item = item
        self._next = None
        self._prev = None


class DLinkList(object):
    """双向链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur._next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur._item)
            cur = cur._next
        print("")

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node._next = self._head
            # 将_head的头节点的prev指向node
            self._head._prev = node
            # 将_head 指向node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur._next != None:
                cur = cur._next
            # 将尾节点cur的next指向node
            cur._next = node
            # 将node的prev指向cur
            node._prev = cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur != None:
            if cur._item == item:
                return True
            cur = cur._next
        return False

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
            # 将node的prev指向cur
            node._prev = cur
            # 将node的next指向cur的下一个节点
            node._next = cur._next
            # 将cur的下一个节点的prev指向node
            cur._next._prev = node
            # 将cur的next指向node
            cur._next = node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur._item == item:
                # 如果首节点的元素即是要删除的元素
                if cur._next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur._next._prev = None
                    # 将_head指向第二个节点
                    self._head = cur._next
                return
            while cur != None:
                if cur._item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur._prev._next = cur._next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur._next._prev = cur._prev
                    break
                cur = cur._next


if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
