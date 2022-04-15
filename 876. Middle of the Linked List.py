# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # when fast reaches the end, slow readhes the middle
        # this will save more memory usage compared to stupid iteration
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
