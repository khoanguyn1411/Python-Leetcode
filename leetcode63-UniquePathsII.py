from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        obs = []

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ob_x = i
                    ob_y = j
                    obs.append([ob_x, ob_y])

        def recurse(x, y):
            if [x, y] in obs:
                return 0

            if x == m - 1 and y == n - 1:
                return 1

            if (x, y) in memo:
                return memo[(x, y)]

            paths = 0

            if x < m - 1:
                paths += recurse(x + 1, y)
            if y < n - 1:
                paths += recurse(x, y + 1)
            memo[(x, y)] = paths
            return paths

        return recurse(0, 0)


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# print(Solution().uniquePathsWithObstacles([[[0, 0], [1, 1], [0, 0]]]))
