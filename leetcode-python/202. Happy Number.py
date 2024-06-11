class Solution:
    def isHappy(self, n: int) -> bool:
        # 只需判断是否会进入循环即可
        # 也就是如果当前n曾经出现过，那就说明进入了循环
        # 跳出条件是变成1
        nums = dict()
        nums[n] = "yes"
        while True:
            if n == 1:
                return True

            n = sum([int(i) ** 2 for i in str(n)])

            if nums.get(n, "no") == "no":
                nums[n] = "yes"
            else:
                return False
