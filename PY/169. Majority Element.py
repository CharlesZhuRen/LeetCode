class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 方法一: 哈希, O(n), O(n), 20%
        # import collections
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)

        # 方法二: 排序, 下标为n/2的元素一定是众数, O(nlogn), O(logn), 80%
        # nums.sort()
        # return nums[len(nums)//2]

        # 方法三: 随机化, O(n), O(1), 90%
        # import random
        # majority_count = len(nums) // 2
        # while True:
        #     candidate = random.choice(nums)
        #     if sum(1 for elem in nums if elem == candidate) > majority_count:
        #         return candidate

        # 方法四: 分治, 左半部分的众数和右半部分的众数中必有一个是真正的众数, O(nlogn), O(logn), 5%
        # def majority_element_rec(l, r):
        #     if l == r:
        #         return nums[l]
        #
        #     mid = (r - l) // 2 + l
        #     left = majority_element_rec(l, mid)
        #     right = majority_element_rec(mid+1, r)
        #
        #     if left == right:
        #         return left
        #
        #     left_count = sum(1 for i in range(l, r + 1) if nums[i] == left)
        #     right_count = sum(1 for i in range(l, r + 1) if nums[i] == right)
        #
        #     return left if left_count > right_count else right
        #
        # return majority_element_rec(0, len(nums)-1)

        # 方法五: boyer-moore投票算法, O(n), O(1), 90%
        # 少数派会互相厮杀殆尽, 存留的必然是众数
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
