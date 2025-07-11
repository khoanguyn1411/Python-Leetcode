from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


solution = Solution()
solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
