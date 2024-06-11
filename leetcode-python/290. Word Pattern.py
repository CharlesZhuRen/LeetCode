class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        alpha = dict()
        count = 0
        pp = []
        for c in pattern:
            if c not in alpha.keys():
                alpha[c] = count
                count += 1
            pp.append(alpha[c])

        count = 0
        alpha = dict()
        words = s.split()
        sp = []
        for word in words:
            if word not in alpha.keys():
                alpha[word] = count
                count += 1

            sp.append(alpha[word])

        return sp == pp