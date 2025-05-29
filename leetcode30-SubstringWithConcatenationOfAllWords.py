from collections import Counter


# class Solution:
#     def findSubstring(self, s: str, words: list[str]) -> list[int]:
#         if not s or not words:
#             return []

#         word_len = len(words[0])
#         word_count = Counter(words)
#         result = []

#         for i in range(word_len):
#             left = i
#             right = i
#             curr_count = Counter()
#             count = 0

#             while right + word_len <= len(s):
#                 word = s[right:right + word_len]
#                 right += word_len

#                 if word in word_count:
#                     curr_count[word] += 1
#                     count += 1

#                     while curr_count[word] > word_count[word]:
#                         left_word = s[left:left + word_len]
#                         curr_count[left_word] -= 1
#                         count -= 1
#                         left += word_len

#                     if count == len(words):
#                         result.append(left)
#                 else:
#                     curr_count.clear()
#                     count = 0
#                     left = right
#                     print(i, left, right)

#         return result


# Cannot do this way since replace method will replace some wrong index of text.
# class Solution:
#     def findSubstring(self, s: str, words: list[str]) -> list[int]:
#         if not s or not words:
#             return []

#         word_len = len(words[0])
#         word_count = Counter(words)
#         total_word_count = word_len * len(words)
#         result = []

#         for i in range(0, len(s) - total_word_count + 1, 1):
#             word_count = Counter(words)
#             text = s[i: i + total_word_count]
#             for word in words:
#                 if i == 1:
#                     print("textCheck", text, word)
#                 if word in text:
#                     word_count[word] -= 1
#                     text = text.replace(word, "", 1)
#                     if i == 1:
#                         print(text)
#             if any(n != 0 for n in word_count.values()):
#                 continue
#             result.append(i)
#         return result


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:


solution = Solution()
print(solution.findSubstring("ababaab", ["ab", "ba", "ba"]))
# print(solution.findSubstring("wordgoodgoodgoodbestword",
#       ["word", "good", "best", "word"]))
