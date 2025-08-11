from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        left = {"x": m - 1, "y": 0}
        right = {"x": m - 1, "y": n - 1}

        while right["y"] > left["y"]:
            middle = {"x": m - 1, "y": (left["y"] + right["y"]) // 2}

            if middle == left or middle == right:
                return (target in matrix[left["y"]]) or (target in matrix[right["y"]])

            if matrix[middle["y"]][middle["x"]] == target:
                return True
            if matrix[left["y"]][left["x"]] < target < matrix[middle["y"]][middle["x"]]:
                right["y"] = middle["y"]
                continue

            if matrix[middle["y"]][middle["x"]] < target < matrix[right["y"]][right["x"]]:
                left["y"] = middle["y"]
                continue
            return (target in matrix[left["y"]]) or (target in matrix[right["y"]])

        return (target in matrix[left["y"]]) or (target in matrix[right["y"]])


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
