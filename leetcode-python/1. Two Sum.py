class Solution:
    def twoSum(self, nums: list[int], target: int) -> tuple[int, int]:
        d = dict() # num: index of num

        # 只遍历一次，这样就解决了数字数值相同但是位置不同的问题，反正两个数必然一前一后被写入dict
        for i, num in enumerate(nums):

            sub = target - num

            if d.get(sub) is not None:
                return d[sub], i
            else:
                d[num] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[2, 7, 11, 15], target=9))
    print(s.twoSum(nums=[3, 2, 4], target=6))
