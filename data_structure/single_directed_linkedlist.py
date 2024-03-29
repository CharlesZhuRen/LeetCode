# 链表能够实现对内存的动态管理, 进行扩充时不需要进行数据的搬迁, 也不需要预先知道数据的大小来申请连续的存储空间

class SingleNode(object):
    """单链表的结点"""

    def __init__(self, item):
        # _item存放数据元素
        self._item = item
        # _next是下一个节点的标识
        self._next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
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
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node._next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur._next != None:
                cur = cur._next
            cur._next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre._next
            # 先将新节点node的next指向插入位置的节点
            node._next = pre._next
            # 将插入位置的前一个节点的next指向新节点
            pre._next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur._item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur._next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur._next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur._next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur._item == item:
                return True
            cur = cur._next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:", ll.length())
    print("travel")
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:", ll.length())
    print("travel")
    ll.travel()