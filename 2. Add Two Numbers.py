# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0  # num1: the number l1 represents, num2: the number l2 represents
        dummy = cur = ListNode(0)  # the list to be returned
        ten = 0  # digit

        # iterate list1 and list2, convert list to int num
        while l1 or l2:
            if l1:
                num1 += l1.val * pow(10, ten)
                l1 = l1.next
            if l2:
                num2 += l2.val * pow(10, ten)
                l2 = l2.next

            ten += 1

        # iterate the sum, convert int num to list
        for num in str(num1 + num2)[::-1]:
            cur.next = ListNode(int(num))
            cur = cur.next

        return dummy.next
