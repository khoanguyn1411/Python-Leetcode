from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findPosition(isFirst):
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    pos = mid
                    if isFirst:
                        right = mid - 1  # search on the left side
                    else:
                        left = mid + 1   # search on the right side
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return pos

        left = findPosition(True)
        right = findPosition(False)
        return [left, right]


solution = Solution()
print(solution.searchRange([2, 2], 2))
