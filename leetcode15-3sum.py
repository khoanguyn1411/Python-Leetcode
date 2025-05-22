from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sums = []

#         for index, num in enumerate(nums):
#             sum2 = 0 - num
#             for index2, num2 in enumerate(nums[index + 1:]):
#                 # print(num, num2, nums[index + 1:])
#                 nums_to_check = nums[index + 1:]
#                 nums_to_check.remove(num2)
#                 if sum2 - num2 in nums_to_check:
#                     new_sum = [num, num2, sum2 - num2]
#                     new_sum.sort()
#                     if new_sum not in sums:
#                         sums.append(new_sum)
#         return sums

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


solution = Solution()
# print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
# print(solution.threeSum([0, 0, 0, 0]))
# print(solution.threeSum(
#     [0, -2, -5, 0]))
# print(solution.threeSum(
#     [0, 2, 0, -10]))

# print(solution.threeSum(
#     [2, 0, -2, 0, -10]))

print(solution.threeSum(
    [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))
