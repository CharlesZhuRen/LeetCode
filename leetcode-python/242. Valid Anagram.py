class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = dict()
        for c in s:
            if c in alpha.keys():
                alpha[c] += 1
            else:
                alpha[c] = 1

        for c in t:
            if c in alpha.keys():
                alpha[c] -= 1
            else:
                return False

        for value in alpha.values():
            if value != 0:
                return False

        return True