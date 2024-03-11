class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = ""
        for word in words:
            res += word[::-1]
            res += " "
        res = res[:-1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
    print(s.reverseWords("God Ding"))
