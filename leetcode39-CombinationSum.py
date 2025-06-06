from typing import List


class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(combo: List, remain_sum, start):
            if remain_sum == 0:
                result.append(list(combo))
                return
            elif remain_sum < 0:
                return
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(combo, remain_sum - candidates[i], i)
                combo.pop()

        backtrack([], target, 0)
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
