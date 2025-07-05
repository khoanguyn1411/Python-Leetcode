from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


solution = Solution()
print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(solution.rotate(
#     [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
