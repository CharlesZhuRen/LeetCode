class Solution:
    def trap(self, height: list[int]) -> int:
        # 对于下标i，下雨后水能到达的最大高度等于下标 i 两边的最大高度的最小值
        # 下标i处能接的雨水量等于下标 i 处的水能到达的最大高度减去height[i]

        # 方法一：动态规划

        if not height:
            return 0

        # leftmax[i] = i位置左边最大高度
        # rightmax[i] = i位置右边的最大高度

        n = len(height)

        # 从左到右记录leftmax
        leftMax = [height[0]] + [0] * (n - 1)  # 0位置的leftmax=height[0]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # 从右到左记录rightmax
        rightMax = [0] * (n - 1) + [height[n - 1]]  # n-1位置的rightmax=height[n-1]

        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        # 为每个i计算能够接住的水的高度
        ans = 0

        for i in range(n):
            ans += min(leftMax[i], rightMax[i]) - height[i]

        return ans


