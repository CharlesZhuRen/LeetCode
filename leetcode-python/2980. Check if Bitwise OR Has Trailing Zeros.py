class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # 只有0|0==0，因此要判断是否存在至少两个偶数
        return len(nums) - sum(x % 2 for x in nums) >= 2