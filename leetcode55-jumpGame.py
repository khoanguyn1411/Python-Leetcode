from typing import List

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = [False] * n
#         dp[0] = True  # start position is always reachable

#         for i in range(n):
#             if dp[i]:  # only proceed if this index is reachable
#                 max_jump = nums[i]
#                 for j in range(i + 1, min(i + max_jump + 1, n)):
#                     dp[j] = True
#                     if j == n - 1:
#                         return True  # early exit if we reach the last index

#         return dp[n - 1]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)

        return True


solution = Solution()
solution.canJump([2, 3, 1, 1, 4])
