class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 96% 神！

        # 处理边界情况
        if intervals == []: return []
        if len(intervals) == 1: return intervals
        # 重叠 == 区间a的右端点 >= 区间b的左断点 并且区间a的左端点 <= 区间b的右端点
        # 先按照左端点排序
        intervals.sort(key=lambda x: x[0])
        # 反之，则不重叠
        current = intervals[0]  # 初始化当前被用来比较的区间
        res = []
        for interval in intervals[1:]:
            if current[1] >= interval[0]:  # 重叠
                # 更新当前区间
                current = [min(current[0], interval[0]), max(interval[1], current[1])]
            else:
                # 添加当前区间到res
                res.append(current)
                # 更新当前区间
                current = interval

        res.append(current)

        return res
