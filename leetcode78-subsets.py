from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(combination: List[int], start: int):

            if start > n:
                return

            result.append(combination.copy())

            for i in range(start, n):
                combination.append(nums[i])
                backtrack(combination, i + 1)
                combination.pop()

        backtrack([], 0)
        return result


print(Solution().subsets([1, 2, 3]))
