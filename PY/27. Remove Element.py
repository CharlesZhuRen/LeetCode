class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 方法一: 双指针, 把不等于val的值保留, 也就实现了把等于val的值去掉
        # left = 0
        # n = len(nums)
        # for right in range(n):
        #     if nums[right] != val:
        #         nums[left] = nums[right]
        #         left += 1
        # return left

        # 方法二: 双指针优化: 避免了重复赋值
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left
