
from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index, num in enumerate(nums):
#             if (target - num) in nums:
#                 subtraction_from_target_index = nums.index(target - num)
#                 if subtraction_from_target_index == index:
#                     continue
#                 if index < subtraction_from_target_index:
#                     return [index, subtraction_from_target_index]
#                 return [subtraction_from_target_index, index]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            subtract = target - num
            if subtract in nums:
                index_after = nums.index(subtract)
                if index_after == index:
                    continue
                return [index, index_after] if index_after > index else [index_after, index]


solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
