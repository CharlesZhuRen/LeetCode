class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # so that it won't do duplicate rotation
        nums[:] = nums[n - k:] + nums[:n - k]
        # note that "nums[:] =" is different from "nums ="
        # the former works while the latter doesn't
        # "nums[:]="是对外部传入对nums进行切片赋值操作，"num="是在函数内部创建了一个局部变量，对外部对nums没有影响

        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2, 3], 1)
    s.rotate([1, 2, 3], 4)
