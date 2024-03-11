class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def getPattern(s: str):
            count = 0
            alpha = dict()  # key=c, value=第一次出现的位置
            for c in s:
                if c not in alpha.keys():  # 首次出现
                    alpha[c] = count
                    count += 1

            # 转化为pattern
            pattern = []

            for c in s:
                pattern.append(alpha[c])

            return pattern

        sp = getPattern(s)
        tp = getPattern(t)

        print(sp)
        print(tp)

        return sp == tp
