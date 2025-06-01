from typing import List


class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                # not i+1 because we can reuse same number
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()  # backtrack

        backtrack(target, [], 0)
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))
