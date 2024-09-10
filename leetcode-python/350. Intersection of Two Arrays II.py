class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        # 统计次数
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        # 求交集
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set1.intersection(set2)
        # 返回
        res = []
        for num in inter:
            appear = min(counter1[num], counter2[num])
            res += [num] * appear
        return res