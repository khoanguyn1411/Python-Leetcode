from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(0, len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps


solution = Solution()
print(solution.jump([2, 3, 1, 1, 4]))
