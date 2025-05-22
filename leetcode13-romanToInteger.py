# class Solution:
#     def romanToInt(self, s: str) -> int:
#         hmap = {
#             'I': 1,
#             'IV': 4,
#             'V': 5,
#             'IX': 9,
#             'X': 10,
#             'XL': 40,
#             'L': 50,
#             'XC': 90,
#             'C': 100,
#             'CD': 400,
#             'D': 500,
#             'CM': 900,
#             'M': 1000
#         }
#         start = 0
#         num = 0
#         while start < len(s):
#             is_subtractive_form_c = start + 1 < len(s) and s[start] == "C" and (
#                 s[start + 1] == "M" or s[start + 1] == "D")
#             is_subtractive_form_x = start + 1 < len(s) and s[start] == "X" and (
#                 s[start + 1] == "C" or s[start + 1] == "L")
#             is_subtractive_form_i = start + 1 < len(s) and s[start] == "I" and (
#                 s[start + 1] == "X" or s[start + 1] == "V")

#             if is_subtractive_form_c or is_subtractive_form_i or is_subtractive_form_x:
#                 num += hmap[s[start: start + 2]]
#                 start = start + 2
#             else:
#                 num += hmap[s[start]]
#                 start = start + 1
#         return num


# class Solution:
#     def romanToInt(self, s):
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         total = 0
#         after = 0

#         for i, char in enumerate(s):
#             after = roman_map[s[i + 1]] if i + 1 < len(s) else 0
#             if roman_map[char] >= after:
#                 total += roman_map[char]
#             else:
#                 total -= roman_map[char]
#         return total


class Solution:
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        after = 0

        for i in range(len(s)):
            after = i + 1
            if after < len(s) and roman_map[s[i]] < roman_map[s[after]]:
                total = total - roman_map[s[i]]
            else:
                total = total + roman_map[s[i]]
        return total


solution = Solution()
print(solution.romanToInt("MCMXCIV"))
