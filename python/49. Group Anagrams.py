class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 本来想hash一个hash表 但是不行
        # 只能将hash表转换成别的形式去hash
        # 可哈希的对象和不可哈希的对象：https://cloud.tencent.com/developer/article/1534815

        alphas = dict()
        for s in strs:
            alpha = dict()
            for c in s:
                if c in alpha.keys():
                    alpha[c] += 1
                else:
                    alpha[c] = 1

            new_a = []
            for key in alpha.keys():
                new_a.append(key)

            new_a.sort()

            pattern = ""

            for a in new_a:
                pattern += a
                pattern += str(alpha[a])

            if pattern not in alphas.keys():
                alphas[pattern] = [s]
            else:
                alphas[pattern].append(s)

        res = []
        for value in alphas.values():
            res.append(value)

        return res
