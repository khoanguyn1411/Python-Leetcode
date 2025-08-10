from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            # If word1 is empty, insert all chars of word2
            if i == len(word1):
                return len(word2) - j
            # If word2 is empty, delete all chars of word1
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)  # no cost
            else:
                return 1 + min(
                    dp(i + 1, j),     # delete
                    dp(i, j + 1),     # insert
                    dp(i + 1, j + 1)  # replace
                )

        return dp(0, 0)


print(Solution().minDistance("horse", "ros"))  # Output: 3
