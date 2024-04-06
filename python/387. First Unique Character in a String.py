import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        # candidate = []
        # for c, num in counter.items():
        #     if num == 1:
        #         candidate.append(c)

        # min_idx = -1

        # for c in candidate:
        #     idx = s.index(c)
        #     if min_idx == -1:
        #         min_idx = idx
        #     elif idx < min_idx:
        #         min_idx = idx

        # return min_idx

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
