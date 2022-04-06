class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 0: no need to move, so return 0
        if m <= 0 or n <= 0:
            return 0
        # initialize the 2-d array
        # the init itself cost O(n^2) time, lol
        dp = [[0 for i in range(n)] for i in range(m)]
        # down: only one way
        for i in range(m):
            dp[i][0] = 1
        # right: only one way
        for i in range(n):
            dp[0][i] = 1
        # compute ways to other goals and to the destination in the end
        # for rach (0, 0) -> (i, j), there are (0, 0)->(i-1, j)->(i, j) and (0, 0)->(i, j-1)->(i, j)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
    print(s.uniquePaths(3, 2))
