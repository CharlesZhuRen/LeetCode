class Solution:
    def countPrimes(self, n: int) -> int:
        # def is_prime(a):
        #     if a == 1 or a == 0:
        #         return False

        #     for i in range(2, int(a**0.5)+1):
        #         if a % i == 0:
        #             return False

        #     return True

        # count = 0

        # for i in range(n):
        #     if is_prime(i):
        #         count += 1

        # return count

        primes = [1] * n
        count = 0
        for i in range(2, n):
            if primes[i] == 1:
                count += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        primes[j] = 0
            print(i, primes)
        return count


if __name__ == '__main__':
    s = Solution()
    n = 10
    s.countPrimes(10)