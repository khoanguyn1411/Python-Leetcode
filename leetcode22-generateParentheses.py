from typing import List


# class Solution:

#     def isValid(self, s: str) -> bool:
#         stack = []
#         bracket_map = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }

#         for char in s:
#             if char not in bracket_map:
#                 stack.append(char)
#             else:
#                 top_element = stack.pop() if stack else "#"
#                 if top_element != bracket_map[char]:
#                     return False
#         return not stack

#     def generateParenthesis(self, n: int) -> List[str]:
#         pairs = []

#         def recurse(pair):
#             if len(pair) == n * 2:
#                 if self.isValid(pair):
#                     pairs.append(pair)
#                 return
#             recurse(pair + "(")
#             recurse(pair + ")")

#         recurse("(")
#         return pairs


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


solution = Solution()
print(solution.generateParenthesis(3))
