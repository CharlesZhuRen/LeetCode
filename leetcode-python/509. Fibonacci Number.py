class Solution:
    def fib(self, n: int) -> int:
        # if n <= 1:
        #     return n

        # return self.fib(n-1) + self.fib(n-2)

        if n < 2:
            return n

        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]
