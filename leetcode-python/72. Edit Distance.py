class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for i in range(m + 1)]
        # 最终目的：把s1的前n个字符变成s2的前m个字符

        # 初始化边界条件，dp[i][0]表示把s1的前i个字符变成空串的操作次数
        for i in range(1, m + 1):
            dp[i][0] = i

        # dp[0][j]表示把空串变成s2的前j个字符的操作次数
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 如果对应位置的字符相同
                    dp[i][j] = dp[i - 1][j - 1]  # 操作次数不变
                else:
                    # 选取修改、插入、删除三种操作里的最小值
                    # 修改：dp[i-1][j-1]+1，在i-1，j-1的基础上变换到i，j
                    # 插入：dp[i][j-1]+1，在i，j-1的基础上变换到i，j
                    # 删除：dp[i-1][j]+1，在i-1，j的基础上变换到i，j
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[-1][-1]