from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len2 = len(word2)

        word1 = [char for char in word1]
        word2 = [char for char in word2]

        smallest = float("inf")

        if not word1 or not word2:
            return 0

        def backtrack(word: List[str], current_step):
            nonlocal smallest
            if word == word2:
                return

            if len(word) > len2:
                for i in range(len(word)):
                    removed_char = word.pop(i)
                    backtrack(word, current_step + 1)
                    word.insert(i, removed_char)
                return

            if len(word) < len2:
                for i in range(len2):
                    for k in range(len(word) + 1):
                        word.insert(k, word2[i])
                        backtrack(word, current_step + 1)
                        word.pop(k)
                return

            steps = 0
            for i in range(len(word)):
                if word[i] == word2[i]:
                    continue
                word[i] = word2[i]
                steps += 1
            current_step += steps
            smallest = min(current_step, smallest)
            return

        backtrack(word1, 0)
        return smallest


print(Solution().minDistance("ros", "horse"))
