class Solution:
    def climbStairs(self, n: int) -> int:
        # initial values: 0: 0, 1: 1, 2: 2(0->2, 0->1->2)
        if n <= 2:
            return n
        # if n > 2: dp
        dp = [0, 1, 2]
        # 0->n == 0->n-1->n + 0->n-2->n
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(0))
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(6))
    print(s.climbStairs(100))
