class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # beat 96% 太牛逼了

        # 记录间断点即可
        # 若第i个点和第i-1个点不连续，则第i个点记录为断点，也就是新的区间的起点
        # 而第i-1个点自动变成上一个区间的结束点
        if nums == []: return []

        start = nums[0]  # value of start
        end = nums[0]  # value of end
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] != nums[i - 1] + 1:
                # 断了，更新结束点
                end = nums[i - 1]
                if start != nums[i - 1]:  # 如果起始点不等于当前点
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start))
                # 更新初始点
                start = nums[i]

        # 处理结尾
        if len(nums) >= 2 and nums[-1] == nums[-2] + 1:  # 如果连续
            res.append(str(start) + "->" + str(nums[-1]))
        else:  # 中断：
            res.append(str(nums[-1]))

        return res
