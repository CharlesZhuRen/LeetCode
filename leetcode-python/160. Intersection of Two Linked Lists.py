# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        temp = headA
        while temp:
            # 注意这个集合里加的是节点
            visited.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None
