class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # write your code here
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            # the definition of mid in official solution is:
            # mid = left + (right - left) // 2
            # but that takes 50% more memory usage
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
