from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(combination: List[int], start: int):

            if len(combination) == k:
                result.append(combination.copy())
                return

            for i in range(start, n + 1):
                combination.append(i)
                backtrack(combination, i + 1)
                combination.pop(-1)

        backtrack([], 1)
        return result


print(Solution().combine(4, 2))
