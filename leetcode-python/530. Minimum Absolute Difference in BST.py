# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = -1
        ans = float('inf')

        def dfs(root):
            nonlocal pre
            nonlocal ans
            if not root:
                return

            dfs(root.left)

            if pre == -1:
                pre = root.val
            else:
                ans = min(ans, root.val - pre)
                pre = root.val

            dfs(root.right)

        dfs(root)

        return ans
