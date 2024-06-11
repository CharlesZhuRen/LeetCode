class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [i for i in s if i.isalpha() or i.isdigit()]  # 之前用过但是忘掉了 包括isspace也忘掉了

        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
