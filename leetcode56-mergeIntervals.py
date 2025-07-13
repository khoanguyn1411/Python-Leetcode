from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        # Step 1: Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])

        result = []
        for i in range(n):
            if i < n - 1 and (intervals[i][0] <= intervals[i + 1][0] <= intervals[i][1]
                              or intervals[i][0] <= intervals[i + 1][1] <= intervals[i][1]
                              or intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1]
                              or intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1]
                              ):
                new_array = intervals[i] + intervals[i + 1]
                new_array.sort()
                new_entity = [new_array[0], new_array[3]]
                intervals[i + 1] = new_entity
            else:
                result.append(intervals[i])
        return result


solution = Solution()
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(solution.merge([[1, 4], [1, 5]]))
