class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        n = len(strs)
        min_len = 100000000000
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        print(min_len)

        prefix = ""
        flag = 1
        for j in range(min_len):
            temp = strs[0][j]
            for i in range(n):
                if temp != strs[i][j]:
                    flag = 0
                    break

            if flag == 0:
                break

            prefix += temp

        return prefix
