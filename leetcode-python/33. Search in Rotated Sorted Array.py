class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left, right = 0, n - 1

        # 先进行一次二分查找，结束以后，left == right == 断点下标
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        nl, nr = 0, 0

        # 如果target的值在断点到数组末尾之间，就在这一段进行二分查找，否则就在前面一段进行二分查找
        if nums[left] <= target <= nums[-1]:
            nl, nr = left, n - 1
        else:
            nl, nr = 0, left - 1

        while nl <= nr:
            mid = (nl + nr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                nl = mid + 1
            else:
                nr = mid - 1
        return -1
