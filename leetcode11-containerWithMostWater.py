from typing import List


# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         max_area = 0
#         for i, height_i in enumerate(heights, 1):
#             for j, height_j in enumerate(heights, 1):
#                 height_to_get = min(height_i, height_j)
#                 max_area = max(max_area, height_to_get * (j - i))
#         return max_area


# 2 pointers approach.
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([1, 1]))
