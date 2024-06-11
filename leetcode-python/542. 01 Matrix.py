class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        # init dp
        # meaning: dp[i][j] means the min distance between mat[i][j] and a zero
        dp = [[10 ** 9 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
        """
        Remember a dp problem? If a node can only move right and down, find the nearst...
        Here there are no limitations as "right and down"
        But we can try each pair of choices
        i.e. left and up, left and down, right and up, right and down
        For each node, we compare itself with its 4 direct neighbours, and then keep the min choice
        And we always keep the min choice, so that we can get all min choices
        """
        # move right and down from the up left node
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:  # compare itself with its left neighbour+1
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:  # compare itself with its down neighbour+1
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # move left and down from the up right node
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # move right and up from the down left node
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        # move left and up from the down right node
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(s.updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
