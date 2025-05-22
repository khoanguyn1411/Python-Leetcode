from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = nums1 + nums2
        list.sort()
        if len(list) % 2 == 0:
            return (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
        return list[len(list) // 2]


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
