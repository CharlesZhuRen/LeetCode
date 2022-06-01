from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        d1 = Counter()  # use a counter dict to record: 'char': num of appearance
        for char in s1:  # init the counter for s1
            d1[char] += 1
        # iterate each substring in s2, each of them has the same length as s1
        for i in range(len(s2) - length + 1):
            sub = s2[i:i + length]
            d2 = Counter()
            for char in sub:  # generate substring's counter
                d2[char] += 1
            if d1 == d2:  # if each pair of <char:num> in sub and s1, then True
                return True
        return False


if __name__ == '__main__':
    # The time cost is terrible(~5%) but the memory usage cost is excellent(95%+)
    s = Solution()
    print(s.checkInclusion(s1='hello', s2='ooolleoooleh'))
    print(s.checkInclusion(s1="ab", s2="eidbaooo"))
