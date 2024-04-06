class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        mx = values[0] + 0
        for i in range(1, len(values)):
            ans = max(ans, mx + values[i] - i)
            mx = max(mx, values[i] + i)

        return ans
