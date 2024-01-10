class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_distance = 0  # 最远可以到达的位置
        n = len(nums)
        for i in range(n):
            if i <= max_distance:  # 当前位置可达
                max_distance = max(max_distance, i + nums[i])  # 若当前位置+当前最大步数>最远可达位置, 则更新最远可达位置
                if max_distance >= n - 1:  # 若最远可达位置 >= 终点位置
                    return True

        return False
