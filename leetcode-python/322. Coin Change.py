class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        F(i) = minF(i-cj) + 1， 1就是目前这枚硬币算一个

        dp[i] = 凑成i元需要的最少硬币数量

        dp[0] = 0 表示凑成0元需要0个硬币
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):  # 从coin开始是因为小于coin的额度就不能使用coin面值的硬币了
                dp[x] = min(dp[x], dp[x - coin] + 1)  # 不使用当前硬币 or 使用当前硬币

        return dp[amount] if dp[amount] != float('inf') else -1
