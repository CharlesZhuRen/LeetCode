class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn, maxn = min(nums), max(nums)
        return math.gcd(minn, maxn)
