class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = res = ''
        for i in s:
            if i not in sub:  # if it won't bring dup char to current sub
                sub += i      # add it to the current sub
            else:
                if len(res) <= len(sub):  # if current sub has been longer than res
                    res = sub             # replace res by sub, then res is the longest sub till now
                sub = sub.split(i)[-1] + i
                # split(i): use current char to split sub, to get a list
                # i.e. sub='pawek', i='w' -> ['pa', 'ek']
                # [-1]: get the last subsub
                # +i: construct a new "current sub"
        return max(len(res), len(sub))  # test case for max: when the length of s is 1


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
