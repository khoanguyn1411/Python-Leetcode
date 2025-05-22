from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nums.sort()
        two_sums_combinations = []
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                new_2_sum_combinations = [nums[i], nums[i + j + 1]]
                if new_2_sum_combinations not in two_sums_combinations:
                    two_sums_combinations.append(new_2_sum_combinations)
        for two_sums in two_sums_combinations:
            total = two_sums[0] + two_sums[1]
            cloned_nums = nums.copy()
            cloned_nums.remove(two_sums[0])
            cloned_nums.remove(two_sums[1])
            left = 0
            right = len(cloned_nums) - 1
            while left < right:
                four_sum = total + cloned_nums[left] + cloned_nums[right]
                if four_sum == target:
                    new_combination = [two_sums[0], two_sums[1],
                                       cloned_nums[left], cloned_nums[right]]
                    new_combination.sort()
                    if new_combination not in combinations:
                        combinations.append(new_combination)
                    while left < right and cloned_nums[left] == cloned_nums[left + 1]:
                        left += 1
                    while left < right and cloned_nums[right] == cloned_nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif four_sum < target:
                    left += 1
                else:
                    right -= 1

        return combinations


solution = Solution()
print(solution.fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0))
