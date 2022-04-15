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
        1. iterate the linkedlist
        2. reverse order of values
        3. reconstruct the linkedlist and then return it
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        dummy = cur = ListNode(0)
        for value in values[::-1]:
            cur.next = ListNode(value)
            cur = cur.next
        return dummy.next
