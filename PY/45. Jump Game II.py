class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)

        # 方法一: 反向查找出发位置, O(n^2), 20%
        # pos = n - 1
        # step = 0
        # while pos > 0:
        #     for i in range(pos):  # 从左到右遍历是为了找到距离后一个位置距离最远的那个位置
        #         if i + nums[i] >= pos:
        #             pos = i  # 此时从后面跳到前面
        #             step += 1
        #             break

        # return step

        # 方法二: 正向
        maxPos, end, step = 0, 0, 0  # 最大可达位置, 边界, 步数

        for i in range(n - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos  # 到达边界以后更新边界, 并进行跳跃
                step += 1

        return step
