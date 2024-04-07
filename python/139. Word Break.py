class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        leetcode_ -> dp = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        i = 0, j = 4, leet in wordDict, dp[0] = 1, so dp[4] = 1
        i = 4, j = 8, code in wordDict, dp[4] = 1, so dp[8] = 1
        :param s:
        :param wordDict:
        :return:
        """
        s = s + ' '
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(n):
            for j in range(i, n):
                # print(i, j)
                # print(s[i:j])
                if dp[i] == 1 and s[i:j] in wordDict:
                    # print(s[i:j])
                    dp[j] = 1

        return True if dp[-1] else False