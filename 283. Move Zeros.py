class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1

        # count_zero = 0
        # not_zero = []
        # for num in nums:
        #     if num == 0:
        #         count_zero += 1
        #     else:
        #         not_zero.append(num)
        # zeros = [0 for i in range(count_zero)]
        # nums[:] = not_zero + zeros

        # Solution 2
        # this takes less memory usage compared to Solution 1
        i = count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            count += 1

        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([1, 0, 0, 1, 2, 3])
