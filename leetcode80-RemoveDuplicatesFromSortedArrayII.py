from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # slow pointer (where to place next valid element)
        slow = 2

        # fast pointer (scan array)
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
