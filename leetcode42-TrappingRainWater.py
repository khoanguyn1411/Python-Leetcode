from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        selected = height[0]
        for h in height:
            if h < selected:
                selected = h


solution = Solution()
solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
