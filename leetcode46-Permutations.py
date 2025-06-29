from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i_added, remaining_list: List[int], combo: List[int]):
            if len(combo) == len(nums):
                result.append(combo)
                return
            combo.append(remaining_list[i_added])
            remaining_list.pop(i_added)
            original_remaining_list = remaining_list.copy()
            original_combo = combo.copy()
            for i in range(len(remaining_list)):
                backtrack(i, remaining_list, combo)
                remaining_list = original_remaining_list
                combo = original_combo

        for i in range(1):
            backtrack(i, nums.copy(), [])

        return result


solution = Solution()
print(solution.permute([1, 2, 3]))
