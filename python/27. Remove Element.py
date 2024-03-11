class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        "方法一: 双指针" \
        "左右指针同时从左边出发" \
        "右指针指向的数不等于val 则赋值给左指针 然后左指针右移一次" \
        "右指针指向的数等于val，则不做操作" \
        "把不等于val的值保留, 也就实现了把等于val的值去掉"
        # left = 0
        # n = len(nums)
        # for right in range(n):
        #     if nums[right] != val:
        #         nums[left] = nums[right]
        #         left += 1
        # return left

        "方法二: 双指针优化: 避免了重复赋值" \
        "右指针从右向左移动" \
        "在两个指针相遇之前" \
        "   若左指针指向的数等于val，则将右指针指向的数赋值给左指针，然后右指针左移，左指针不动" \
        "               否则左指针右移"
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
