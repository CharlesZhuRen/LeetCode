class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        4 conditions for (low, high, result)
        1. odd, even, n/2
        2. odd, odd, n/2+1
        3. even, even, n/2
        4. even, odd, n/2

        And this can be simplified to 2 conditions:
        1. odd, odd
        2. others
        """
        if low % 2 == 1 and high % 2 == 1:
            return int((high - low + 1) / 2) + 1
        else:
            return int((high - low + 1) / 2)


if __name__ == '__main__':
    S = Solution()
    print(S.countOdds(low=3, high=7))
    print(S.countOdds(low=8, high=10))
