class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m <= 0 or n <= 0:
            return 0
        dp = [[0 for i in range(n)] for i in range(m)]
        # for i == 0 or j == 0: cost = grid[i][j]
        for i in range(m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                # use min to find the cheapest path for each node
                # so that we can get the cheapest path to the destination
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # print(dp)
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(s.minPathSum(grid=[[1, 2, 3], [4, 5, 6]]))
