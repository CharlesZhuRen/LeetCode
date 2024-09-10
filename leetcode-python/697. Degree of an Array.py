class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()

        for idx, num in enumerate(nums):
            if num in d:
                d[num][0] += 1
                d[num][2] = idx
            else:
                d[num] = [1, idx, idx]

        maxNum = minLen = 0

        for count, left, right in d.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen > (span := right - left + 1):
                    minLen = span

        return minLen