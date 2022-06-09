class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 != 0:
            return nums[int((m + n) / 2)]
        else:
            return (nums[int((m + n - 1) / 2)] + nums[int((m + n + 1) / 2)]) / 2


"""
1. use list.sort() to meet the requirement of time complexity
2. merge 2 lists and find the median
    - if the length is odd, then just return the median
    - else, compute and return the ave of medians
"""

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
