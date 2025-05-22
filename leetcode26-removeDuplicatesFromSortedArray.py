from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         unique = {}

#         for num in nums:
#             if num not in unique:
#                 unique[num] = 1
#             else:
#                 unique[num] = unique[num] + 1
#         return len(unique.keys())


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
