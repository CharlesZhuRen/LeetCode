class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        left = [0] * n  # 一个数组，每个位置代表ratings中对应位置的孩子所需要的糖果数量
        # 把“相邻的孩子中，评分高的孩子的糖果要更多”拆分成两个规则：
            # 左规则：ratings[i-1] < ratings[i]时，i的糖果要多于i-1的糖果
            # 右规则：ratings[i] > ratings[i+1]时，i的糖果要多于i+1的糖果

        # 从左往右遍历，实现左规则
        for i in range(n):
            # i=0时，给一个就好，i>0且符合左规则时，i的数量是i-1的数量+1
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0

        # 从右往左遍历，实现右规则
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1  # 只要累加就行
            else:
                right = 1
            ret += max(left[i], right)  # 肯定是选大的 不然肯定不够

        return ret