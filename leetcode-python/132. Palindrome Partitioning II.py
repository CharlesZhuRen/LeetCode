class Solution:
    def minCut(self, s: str):
        n = len(s)
        g = [[True] * n for _ in range(n)]

        # 通过dp，遍历所有从i到j的字符串，判断g[i][j]是否是回文串
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        print(g)

        f = [float("inf")] * n

        # 第二次dp
        for i in range(n):
            if g[0][i]:  # 如果0到i是回文串，那么只需要分割0次
                f[i] = 0
            else:
                for j in range(i):  # 如果j+1到i是回文串，那么需要分割的次数就是fi次或fj次加一次里的最小值
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]