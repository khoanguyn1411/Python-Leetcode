from typing import List


# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         if not nums:
#             return []

#         if len(nums) == 1:
#             return nums

#         right = len(nums) - 1
#         left = len(nums) - 2

#         while right >= 0 and left >= 0 and nums[right] <= nums[left]:
#             if left == 0:
#                 right -= 1
#                 left = right - 1
#             else:
#                 left -= 1

#         if right == 0 and left == 0:
#             nums.reverse()
#             return nums
#         else:
#             nums[left], nums[right] = nums[right], nums[left]

# if left + 1 < len(nums):
#     for i in range(left + 1, len(nums), 1):
#         for j in range(i + 1, len(nums), 1):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]

#         return nums


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return []

        n = len(nums)

        if n == 1:
            return nums

        decrease_i = n - 1

        while decrease_i >= 0 and nums[decrease_i] <= nums[decrease_i - 1]:
            decrease_i -= 1

        decrease_i -= 1
        increase_i = decrease_i + 1

        if decrease_i >= 0:
            smallest_i = increase_i
            while increase_i < n:
                if nums[increase_i] < nums[smallest_i] and nums[increase_i] > nums[decrease_i]:
                    smallest_i = increase_i
                increase_i += 1
            increase_i = smallest_i

        nums[decrease_i], nums[increase_i] = nums[increase_i], nums[decrease_i]

        if decrease_i + 1 < len(nums):
            for i in range(decrease_i + 1, len(nums), 1):
                for j in range(i + 1, len(nums), 1):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        return nums


solution = Solution()
# print(solution.nextPermutation([4, 2, 0, 2, 3, 2, 0]))
# print(solution.nextPermutation([2, 3, 1]))
print(solution.nextPermutation([5, 1, 1]))
