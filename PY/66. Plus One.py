class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        # 找到第一个不为9的元素加1, 然后将后续所有元素置为零
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # 如果所有元素均为9, 则返回一个新数组
        return [1] + [0] * n
