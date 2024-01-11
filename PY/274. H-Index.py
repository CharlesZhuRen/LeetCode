class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        # 方法一: 排序后从小到大遍历到h无法继续增大
        # sorted_citation = sorted(citations, reverse=True)
        # h = 0
        # i = 0
        # while i < n and sorted_citation[i] > h:
        #     h += 1
        #     i += 1
        # return h

        # 方法二: 计数排序, 先遍历一次记录每个引用次数出现的次数, 然后从后往前累加得到至少i篇论文被引用至少i次
        counter = [0 for i in range(n + 1)]  # [0, 1, ..., n]
        # 0 <= h <= n
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += counter[i]
            if total >= i:
                return i
