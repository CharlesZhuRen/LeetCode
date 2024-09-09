import collections
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        """
        方法一：迭代
        1. iterate the linkedlist and store values in a queue
        3. pop values from the queue, reconstruct the linkedlist and then return it
        """
        # values = collections.deque()
        # while head:
        #     values.appendleft(head.val)
        #     head = head.next
        # dummy = cur = ListNode(0)
        # while values:
        #     cur.next = ListNode(values.popleft())
        #     cur = cur.next
        # return dummy.next

        """
        方法二：递归
        """
        def recur(cur, pre): # 传入时的顺序：pre, cur, cur.next
            if not cur:
                return pre

            res = recur(cur.next, cur) # cur, cur.next 变为 cur.next cur
            cur.next = pre # cur的next改为pre，此时顺序为res -> cur -> pre
            return res

        return recur(head, None)