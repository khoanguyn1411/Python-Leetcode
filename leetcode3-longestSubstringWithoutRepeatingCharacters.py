# My method

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substring_len = 0
#         for i1, char1 in enumerate(s):
#             continue_char = [char1]
#             for i2 in range(i1 + 1, s.__len__(), 1):
#                 char2 = s[i2]
#                 if char2 not in continue_char:
#                     continue_char.append(char2)
#                 else:
#                     break
#             if continue_char.__len__() > substring_len:
#                 substring_len = continue_char.__len__()

#         return substring_len


# This method called sliding window solution

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_index = {}  # Stores the latest index of each character
#         start = 0  # Start of the current substring
#         max_length = 0

#         for i, char in enumerate(s):
#             if char in char_index and char_index[char] >= start:
#                 # Move start right past the last occurrence
#                 start = char_index[char] + 1

#             char_index[char] = i  # Update the last seen index
#             max_length = max(max_length, i - start + 1)  # Update max length

#         return max_length

# dvdf for testing case char_index[char] >= start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_len = 0

        for index, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            char_index[char] = index
            max_len = max(max_len, index - start + 1)
        return


sol = Solution()
print(sol.lengthOfLongestSubstring("abba"))
# sol.lengthOfLongestSubstring("abcabd")
