from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        i = 0
        n = len(nums)
        count = 0
        while i < n:
            k = 0
            if nums[i] == nums[left]:
                i += 1
                count += 1
                if count < 2:
                    left += 1
            else:
                if count > 2:
                    k = left + 1
                    count = 1
                    while k < i:
                        nums[k] = nums[i]
                        k += 1
                        count += 1
                    k = 0
                    left += 2
                    i += 1
                else:
                    count = 0
                    left = i
                    i += 1
        return left


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
