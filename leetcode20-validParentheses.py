# class Solution:
#     # This solution is valid for this case ([)]
#     def isValid(self, s: str) -> bool:
#         original_len = len(s)
# bracket_map = {
#     "{": "}",
#     "(": ")",
#     "[": "]"
# }
#         if (original_len % 2 == 1):
#             return False
#         left = 0
#         while left < len(s) and s[left] in bracket_map:
#             if s[left] not in bracket_map:
#                 return False
#             right = left + 1
#             while right < len(s):
#                 if bracket_map[s[left]] == s[right]:
#                     s = s.replace(s[right], "")
#                     break
#                 else:
#                     right += 1
#             left += 1
#         return len(s) == original_len // 2

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else "#"
                if top_element != bracket_map[char]:
                    return False
        return not stack


solution = Solution()
print(solution.isValid("((()))"))
