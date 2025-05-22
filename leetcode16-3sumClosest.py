from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = 0
        for i in range(3):
            closest += nums[i]
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total == target:
                    return target
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return closest


solution = Solution()

print(solution.threeSumClosest([-4, -1, 1, 2], 1))
