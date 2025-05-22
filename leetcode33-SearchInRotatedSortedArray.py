from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             # Determine which side is sorted
#             if nums[left] <= nums[mid]:  # Left half is sorted
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1  # Target in left half
#                 else:
#                     left = mid + 1   # Target in right half
#             else:  # Right half is sorted
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1   # Target in right half
#                 else:
#                     right = mid - 1  # Target in left half

#         return -1  # Not found


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


solution = Solution()
print(solution.search([5, 6, 0, 1, 2, 3, 4], 0))
