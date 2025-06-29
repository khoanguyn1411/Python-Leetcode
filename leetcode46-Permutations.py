from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(combo, remaining):
            if len(combo) == len(nums):
                result.append(combo[:])
                return

            for i in range(len(remaining)):
                # Choose
                combo.append(remaining[i])
                val = remaining.pop(i)

                # Explore
                backtrack(combo, remaining)

                # Undo
                combo.pop()
                remaining.insert(i, val)

        backtrack([], nums[:])
        return result


solution = Solution()
print(solution.permute([1, 2, 3]))
