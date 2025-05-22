# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         longest = 0
#         stack = [-1]
#         for (index, char) in enumerate(s):
#             if char == "(":
#                 stack.append(index)
#             else:
#                 stack.pop()
#                 if not stack:
#                     stack.append(index)
#                 else:
#                     longest = max(longest, index - stack[-1])
#                     print(stack[-1])
#         return longest


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        longest = 0

        for (index, char) in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    longest = max(longest, index - stack[-1])
        return longest


solution = Solution()
print(solution.longestValidParentheses("((()"))
