from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         left = 0
#         total = m + n

#         for _ in range(len(nums1) - m):
#             if nums1[-1] == 0:
#                 nums1.pop(-1)

#         if m == 0:
#             while nums2:
#                 nums1.append(nums2[0])
#                 nums2.pop(0)
#             return nums1
#         elif n == 0:
#             return nums1

#         while left < total and nums2:
#             if nums1[left] <= nums2[0]:
#                 if left + 1 >= len(nums1):
#                     nums1.insert(left + 1, nums2[0])
#                     left += 1
#                     nums2.pop(0)
#                 else:
#                     left += 1
#             else:
#                 nums1.insert(left, nums2[0])
#                 nums2.pop(0)
#                 left += 1

#         return nums1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for nums1, nums2, and end position
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining nums2 elements if any
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# print(Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(Solution().merge(nums1=[0], m=0, nums2=[1], n=1))
