class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        current row index从0递增到numrows-1，然后再递减
        所以设置一个flag
        每次i += flag
        需要递减的时候flag=-1，需要递增的时候flag=1
        :param s:
        :param numRows:
        :return:
        """
        if numRows < 2:
            return s

        res = ["" for _ in range(numRows)]

        i = 0
        flag = -1

        for c in s:
            res[i] += c

            if i == 0 or i == numRows - 1:
                flag = - flag

            i += flag

        return "".join(res)
