# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not list1 and not list2:
    #         return None
    #     # dummy: a virtual head node
    #     # cur: a pointer, it will move
    #     # will return dummy.next, which is the head node of the merged list
    #     dummy = cur = ListNode(0)
    #
    #     while list1 and list2:  # both lists have more nodes to iterate
    #         if list1.val < list2.val:  # choose the smaller one as the next node in the merged new list
    #             cur.next = list1
    #             list1 = list1.next  # update the pointer in list1
    #         else:
    #             cur.next = list2
    #             list2 = list2.next  # update the pointer in list2
    #
    #         cur = cur.next  # next one
    #
    #     if not list1:   # nothing left in list1, then just append the remains of list2 to the new list
    #         cur.next = list2
    #     if not list2:
    #         cur.next = list1
    #
    #     return dummy.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
