# class Solution:
#     def climbStairs(self, n: int) -> int:
#         result = 0

#         def recurse(sum):
#             nonlocal result
#             if sum == n:
#                 result += 1
#                 return
#             if sum > n:
#                 return

#             if sum < n:
#                 for i in range(2):
#                     recurse(sum + i + 1)

#         recurse(0)
#         return result


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recurse(sum):
            if sum == n:
                return 1
            if sum > n:
                return 0

            if sum in memo:
                return memo[sum]

            if sum < n:
                total = 0
                for i in range(2):
                    total += recurse(sum + i + 1)
                memo[sum] = total
                return total

        return recurse(0)


print(Solution().climbStairs(3))
