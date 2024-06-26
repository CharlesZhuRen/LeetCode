class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, n):
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))

        return dp[-1]