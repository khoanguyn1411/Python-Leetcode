from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(combo, remaining):
            if len(combo) == len(nums):
                result.append(combo[:])
                return
            unique = []
            for i in range(len(remaining)):
                if remaining[i] not in unique:
                    unique.append(remaining[i])
                else:
                    continue

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
print(solution.permuteUnique([1, 2, 2, 3]))
