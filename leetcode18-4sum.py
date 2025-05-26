from typing import List


class Solution:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()

        def k_sum(start, remaining_k, sum):
            res = []

            # Early termination
            if start == len(nums) or nums[start] * remaining_k > sum or nums[-1] * remaining_k < sum:
                return res

            if remaining_k == 2:
                left, right = start, len(nums) - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total == sum:
                        res.append([nums[left], nums[right]])

                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < sum:
                        left += 1
                    else:
                        right -= 1
                return res

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                for subset in k_sum(i + 1, remaining_k - 1, sum - nums[i]):
                    res.append([nums[i]] + subset)

            return res

        return k_sum(0, k, target)


solution = Solution()
print(solution.kSum([1, 0, -1, 0, -2, 2], 0, 4))
