import collections


class Solution:
    def isValid(self, s: str) -> bool:
        # if the length of s is not even, then it's invalid
        if len(s) % 2 != 0:
            return False

        # mapping between left and right
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # use deque to work as a stack, append to right side, and pop from right side
        stack = collections.deque()

        # iterate each character in s
        for ch in s:
            if ch in pairs:  # if it is a right bracket
                if not stack or stack[-1] != pairs[ch]:
                    # stack is empty (i.e. no matching left bracket)
                    # or the last top of the stack doesn't match current bracket
                    return False

                stack.pop()
            else:  # if it is a left bracket: just append it and let it wait to be matched
                stack.append(ch)

        # after iterating, there shouldn't be any bracket left in the stack
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid(s="()[]{}"))
    print(s.isValid(s="([()])"))
