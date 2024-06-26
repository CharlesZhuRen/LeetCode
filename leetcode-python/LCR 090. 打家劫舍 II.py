class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            n = len(nums)

            if n == 1:
                return nums[0]

            dp = [0 for i in range(n)]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            return dp[-1]

        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        return max(helper(nums[1:]), helper(nums[:-1]))
