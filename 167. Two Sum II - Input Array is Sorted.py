class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]  # asked to return "real index"

            if numbers[i] + numbers[j] < target:  # left should be larger
                i += 1
            elif numbers[i] + numbers[j] > target:  # right should be smaller
                j -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], target=9))
