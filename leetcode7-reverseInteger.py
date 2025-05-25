class Solution:

    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        return result * - 1 if is_negative else result


solution = Solution()
print(solution.reverse(1232))
