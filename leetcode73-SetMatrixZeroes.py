from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zero_pos = {"x": [], "y": []}
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    zero_pos["x"].append(x)
                    zero_pos["y"].append(y)

        for y in range(m):
            if y in zero_pos["y"]:
                for i in range(n):
                    matrix[y][i] = 0

        for x in range(n):
            if x in zero_pos["x"]:
                for i in range(m):
                    matrix[i][x] = 0
        return matrix


# print(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
