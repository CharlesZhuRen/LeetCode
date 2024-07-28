class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]

        res = start

        for num in nums[1:]:
            res = res ^ num

        return res
