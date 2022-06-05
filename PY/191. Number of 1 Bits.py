class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin(): convert n to binary format (composed of 1 and 0), then just count the num of 1
        return bin(n).count("1")


if __name__ == '__main__':
    print(Solution().hammingWeight(n=11))
