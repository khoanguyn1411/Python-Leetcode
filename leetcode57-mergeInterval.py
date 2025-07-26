from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Step 1: Sort intervals by the start time
        intervals.append(newInterval)

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]

            # Step 2: If overlapping, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # extend the end
            else:
                merged.append(current)  # no overlap, new interval

        return merged


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))
