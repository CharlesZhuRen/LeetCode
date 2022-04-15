class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(grid, x, y) -> int:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] != 1:
                # invalid or not island
                return 0
            # yes, it is island, so we first denote it as 0 to avoid duplicate
            grid[x][y] = 0
            ans = 1
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # all its neighbours
                next_i, next_j = x + di, y + dj
                ans += dfs(grid, next_i, next_j)
            return ans

        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(dfs(grid, i, j), ans)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland(grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    print(s.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))
