class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def recurse(x, y):
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

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1] * n for _ in range(m)]

#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]

#         return dp[m-1][n-1]


print(Solution().uniquePaths(3, 7))
