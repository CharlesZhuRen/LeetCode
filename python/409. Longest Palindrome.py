import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0  # 可以构建的最长回文串的长度
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
