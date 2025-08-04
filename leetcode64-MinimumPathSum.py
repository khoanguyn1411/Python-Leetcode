from typing import List


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         m = len(grid)
#         n = len(grid[0])

#         smallest_sum = float("inf")

#         def recurse(current_sum, x, y):
#             nonlocal smallest_sum

#             current_sum += grid[x][y]

#             if x == m - 1 and y == n - 1:
#                 smallest_sum = min(smallest_sum, current_sum)
#                 return

#             if x < m - 1:
#                 recurse(current_sum, x + 1, y)
#             if y < n - 1:
#                 recurse(current_sum, x, y + 1)

#         recurse(0, 0, 0)
#         return smallest_sum


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         m = len(grid)
#         n = len(grid[0])

#         memo = {}
#         smallest_sum = float("inf")

#         def recurse(current_sum, x, y):
#             nonlocal smallest_sum

#             current_sum += grid[x][y]

#             # If current path already worse than smallest_sum, prune

#             if current_sum >= smallest_sum:
#                 return

#             # If reached bottom-right, update smallest_sum
#             if x == m - 1 and y == n - 1:
#                 smallest_sum = min(smallest_sum, current_sum)
#                 return

#             # If we have visited (x, y) with a smaller sum before, prune
#             if (x, y) in memo and memo[(x, y)] <= current_sum:
#                 return

#             memo[(x, y)] = current_sum

#             # Explore neighbors
#             if x < m - 1:
#                 recurse(current_sum, x + 1, y)
#             if y < n - 1:
#                 recurse(current_sum, x, y + 1)

#         recurse(0, 0, 0)
#         return smallest_sum


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         m = len(grid)
#         n = len(grid[0])

#         def recurse(x, y):

#             if x == m - 1 and y == n - 1:
#                 return grid[x][y]

#             right = down = float("inf")

#             if x < m - 1:
#                 down = recurse(x + 1, y)

#             if y < n - 1:
#                 right = recurse(x, y + 1)

#             return grid[x][y] + min(right, down)

#         return recurse(0, 0)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        memo = {}

        def recurse(x, y):

            if x == m - 1 and y == n - 1:
                return grid[x][y]

            # Check memo
            if (x, y) in memo:
                return memo[(x, y)]

            right = down = float("inf")

            if x < m - 1:
                down = recurse(x + 1, y)

            if y < n - 1:
                right = recurse(x, y + 1)

            memo[(x, y)] = grid[x][y] + min(right, down)

            return memo[(x, y)]

        return recurse(0, 0)


# print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))
