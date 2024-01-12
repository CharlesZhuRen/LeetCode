class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1 for i in range(n)]
        beforePro = 1  # 前缀所有数的乘积
        afterPro = 1  # 后缀所有数的乘积

        for i in range(n):
            j = n - 1 - i  # 使用双指针即可同时从前和从后遍历
            answer[i] *= beforePro  # 前缀积赋值给左指针对应的answer
            answer[j] *= afterPro  # 后缀积赋值给右指针对应的answer
            beforePro *= nums[i]  # 前缀积被乘以左指针对应的num
            afterPro *= nums[j]  # 后缀积被乘以右指针对应的num

        return answer
