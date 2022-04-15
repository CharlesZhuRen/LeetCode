# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # a virtual node before head, so that we can:
        #   return dummy.next as head in the end
        #   reach the node left to Nth when another point reaches the end
        dummy = ListNode(0, head)
        first = head
        second = dummy
        # first departs, so that first and second maintain the distance of n
        #   Example: n == 4, list = [1, 2, 3, 4, 5, 6, 7, 8], goal: remove 5
        #   0(second), 1(head), 2, 3, 4, 5(first), 6, 7, 8(end)
        for i in range(n):
            first = first.next
        #   0, 1(head), 2, 3(second), 4, 5, 6, 7, 8(first, end)
        while first:
            first = first.next
            second = second.next
        #   0, 1(head), 2, 3, 4(second), 5, 6, 7, 8(end), None(first)
        second.next = second.next.next
        #   0(dummy), 1(head), 2, 3, 4, 6, 7, 8
        return dummy.next
