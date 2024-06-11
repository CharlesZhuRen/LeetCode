import collections


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        # element in queue: (row_index, col_index, counter)
        queue = collections.deque()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j, 0))

        # yield 4 (or less) direct neighbours of a ndoe in the matrix
        def neighbors(i, j) -> (int, int):
            for ni, nj in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    yield ni, nj

        d = 0  # a counter: how many minutes we take
        """
        Have a think: How does d play a role as a counter?
        1. initially, there are (i, j, d=0) in the queue
        2. after a rotten, a (i, j, d=t) is removed, and a (i+-1, j+-1, d=t+1) is appended
        3. in the end, d is something like "min" total num of minutes for rotten 
        """
        while queue:  # when there are rotten oranges remained to consider
            i, j, d = queue.popleft()
            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1:  # if the neighbour to the rotten orange is a normal orange
                    grid[ni][nj] = 2   # turn it to rotten
                    queue.append((ni, nj, d + 1))  # append it to the queue, consider its neighbours later

        # "impossible" means impossible :)
        if any(1 in row for row in grid):
            return -1

        return d


if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(s.orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(s.orangesRotting(grid=[[0, 2]]))
