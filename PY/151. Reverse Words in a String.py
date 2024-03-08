class Solution:
    def reverseWords(self, s: str) -> str:
        # words = []
        # temp = ""
        # for c in s:
        #     if c == " ":
        #         if temp != "" and not temp.isspace():
        #             words.append(temp)
        #             temp = ""
        #     else:
        #         temp += c

        # if temp != "" and not temp.isspace():
        #     words.append(temp)

        # return " ".join(words[::-1])

        return " ".join(reversed(s.split()))
