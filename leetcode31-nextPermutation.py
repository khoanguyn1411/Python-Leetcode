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
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:

            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums


solution = Solution()
# print(solution.nextPermutation([4, 2, 0, 2, 3, 2, 0]))
# print(solution.nextPermutation([2, 3, 1]))
print(solution.nextPermutation([5, 1, 1]))
