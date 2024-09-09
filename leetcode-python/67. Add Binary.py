class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 方法一：直接进行格式转换
        return "{0:b}".format(int(a, 2) + int(b, 2))
    