class Solution:
    def romanToInt(self, s: str) -> int:
        # 从后往前遍历
        # 若当前字符对应的值小于右边字符对应的值, 则减去当前字符对应的值, 反之加上
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        n = len(s)
        res += map[s[n - 1]]
        for i in range(n - 2, -1, -1):
            if map[s[i]] < map[s[i + 1]]:
                res -= map[s[i]]
            else:
                res += map[s[i]]

        return res
