from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(combo: List, remain, start):
            if remain == 0:
                result.append(list(combo))
            elif remain < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(combo, remain - candidates[i], i + 1)
                combo.pop()

        backtrack([], target, 0)
        return result


solution = Solution()
# print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(solution.combinationSum2([1, 1, 1, 1, 1, 1, 1], 5))
