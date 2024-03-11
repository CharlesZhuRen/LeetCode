class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()  # <num: index>
        for i, num in enumerate(nums):
            if target - num in hashtable:  # the time complexity of look for in hashtable is O(1)
                return [hashtable[target - num], i]  # index of sub, index of num
            hashtable[nums[i]] = i  # the sub is not found, then store <num: index of num>
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[2, 7, 11, 15], target=9))
    print(s.twoSum(nums=[3, 2, 4], target=6))
