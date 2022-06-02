class Solution:
    def average(self, salary: list[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


if __name__ == '__main__':
    S = Solution()
    print(S.average(salary=[4000, 3000, 1000, 2000]))
    print(S.average(salary=[1000, 2000, 3000]))
