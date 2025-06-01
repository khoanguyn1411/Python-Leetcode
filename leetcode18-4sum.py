from typing import List


class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        results = []

        def backtrack(start, k, target, path):
            # Base case: when k == 2, solve 2-sum with two pointers
            if k == 2:
                left, right = start, len(nums) - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum == target:
                        results.append(path + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                return

            # For k > 2, recursively reduce to smaller k
            for i in range(start, len(nums) - k + 1):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Pruning: if the smallest possible sum > target or largest possible sum < target, stop
                if nums[i] * k > target:
                    break
                if nums[-1] * k < target:
                    break

                backtrack(i + 1, k - 1, target - nums[i], path + [nums[i]])

        nums.sort()
        backtrack(0, k, target, [])
        return results


solution = Solution()
print(solution.kSum([1, 0, -1, 0, -2, 2], 0, 4))
