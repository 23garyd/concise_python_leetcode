class Solution:

    '''
    def longestValidParentheses(self, s):
        stack, mx = [], 0
        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
        stack = [-1] + stack + [len(s)]
        for i1, i2 in zip(stack, stack[1:]):
            mx = max(mx, i2 - i1 - 1)
        return mx if len(stack) > 2 else len(s)
    '''

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length

a = Solution()
res = a.longestValidParentheses(")()())")
print(res)