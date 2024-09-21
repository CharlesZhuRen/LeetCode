class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            for j in range(1, n):
                k = (i**2 + j**2)**0.5
                if 1 <= k <= n and k.is_integer():
                    count += 1
        return count