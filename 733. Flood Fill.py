from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:

        # This is a solution based on bfs, which is more inline with my intuition
        # It can also be implemented by dfs: fill, fill, fill...nothing to fill, go back, fill, fill...

        old_color = image[sr][sc]

        # if needless to update...
        if old_color == newColor: return image

        # and we need to know the size of matrix first
        n, m = len(image), len(image[0])

        # init a deque to store (x, y) first
        que = deque([(sr, sc)])  # similar to list, but easier to pop and append

        # update the startpoint first
        image[sr][sc] = newColor

        # when there are grids to be checked
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:  # iterate its four neighbours
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == old_color:  # if valid and need to be updated
                    que.append((mx, my))
                    image[mx][my] = newColor
        return image


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
    print(s.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2))
