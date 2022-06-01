# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # just similar to 704.Binary Search
        # the difference is that this problem prefers the left one in order
        left, right = 1, n

        while left < right:
            mid = int((left + right) / 2)

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

