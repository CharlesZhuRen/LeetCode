class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针
        n = len(nums)

        if n <= 2:
            return n

        fast = slow = 2

        while fast < n:
            if nums[fast] != nums[slow - 2]:  # 快指针指向的数!=慢指针指向数的前面第二个, 也就是保留至多两个重复数
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow