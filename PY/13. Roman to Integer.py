class Solution:
    def romanToInt(self, s: str) -> int:

        s2v = {'M': 1000,
               'D': 500,
               'C': 100,
               'L': 50,
               'X': 10,
               'V': 5,
               'I': 1}

        res = 0

        while len(s) > 0:
            if len(s) > 1:
                if s2v[s[0]] < s2v[s[1]]:
                    res -= s2v[s[0]]
                else:
                    res += s2v[s[0]]
            else:
                res += s2v[s[0]]
            
            s = s[1:]

        return res