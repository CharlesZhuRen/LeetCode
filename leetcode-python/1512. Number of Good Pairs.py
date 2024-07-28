class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        m = Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in m.items())
