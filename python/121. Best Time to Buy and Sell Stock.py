class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        earn = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                current_earn = prices[i] - min_price
                if current_earn > earn:
                    earn = current_earn

        return earn
