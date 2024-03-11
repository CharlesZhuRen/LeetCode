class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        The goal: max f(i)
        where f(i) is the max sum ended with num[i]
        so we need to calculate f(i) for each i
        and then return the max one
        for each f(i)
        we need to consider it should be f(i-1) + i or f(i)
        i.e. Do we need to keep the history?
            if i > history + i, then we just forget history

        the most difficult step here
        is to define f(i):
        How do we realize to define it as the max sum "ended with i"?
        """
        pre, maxAns = 0, nums[0]

        for i in nums:
            pre = max(pre + i, i)  # f(i) ended with current i
            maxAns = max(maxAns, pre)  # the max one

        return maxAns


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
