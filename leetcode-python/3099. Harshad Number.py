class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = list(str(x))
        s = [int(_) for _ in s]
        s = sum(s)
        if x % s == 0:
            return s
        else:
            return -1