class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 快慢指针, 从1位置开始, 快指针遍历到的不重复数填充给慢指针
        n = len(nums)

        if n == 0:
            return n

        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow
