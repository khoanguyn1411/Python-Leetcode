
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            # If word1 is empty, insert all chars of word2
            if i == len(word1):
                return len(word2) - j
            # If word2 is empty, delete all chars of word1
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)  # no cost

            else:
                min_steps = 1 + min(
                    dp(i + 1, j),     # delete
                    dp(i, j + 1),     # insert
                    dp(i + 1, j + 1)  # replace
                )
                memo[(i, j)] = min_steps
                return min_steps

        return dp(0, 0)


print(Solution().minDistance("horse", "ros"))  # Output: 3
