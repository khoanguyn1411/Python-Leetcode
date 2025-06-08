from typing import List


# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums.sort()
#         if nums[0] > 1:
#             return 1
#         if nums[len(nums) - 1] < 1:
#             return 1
#         if len(nums) == 1:
#             if nums[0] != 1:
#                 return 1
#             return nums[0] + 1
#         for i in range(len(nums)):
#             if nums[i] == nums[i - 1] + 1 or nums[i] == nums[i - 1] or nums[i] <= 1:
#                 continue
#             if nums[i - 1] >= 1:
#                 return nums[i - 1] + 1
#             return 1

#         return nums[i] + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                print("Here")
                # Swap nums[i] to its correct position at nums[nums[i] - 1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        print(nums)

        # Step 2: Find the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: All positions are correct, so answer is n + 1
        return n + 1


solution = Solution()
print(solution.firstMissingPositive([1, 2, -1, 4, 2, 5]))
