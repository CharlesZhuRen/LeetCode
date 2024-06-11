class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        nums = [x * x for x in nums]
        return sorted(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
    print(s.sortedSquares([-7, -3, 2, 3, 11]))
