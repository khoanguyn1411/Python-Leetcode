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


print(Solution().uniquePaths(3, 7))
