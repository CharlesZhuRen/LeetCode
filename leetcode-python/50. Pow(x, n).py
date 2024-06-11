class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(n):
            if n == 0:
                return 1.0

            y = qpow(n // 2)

            return y * y if n % 2 == 0 else y * y * x

        return qpow(n) if n >= 0 else 1 / qpow(-n)