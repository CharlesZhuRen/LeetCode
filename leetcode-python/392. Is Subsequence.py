class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(t)
        n = len(s)

        tp = sp = 0

        while sp < n:
            if tp == m:
                return False

            if s[sp] == t[tp]:
                sp += 1

            tp += 1

        return True
