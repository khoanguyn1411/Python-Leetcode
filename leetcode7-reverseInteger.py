class Solution:
    # def reverse(self, x: int) -> int:

    #     str_x = str(abs(x))
    #     result = int(str_x[::-1]) if x > 0 else int(str_x[::-1]) * -1

    #     if result < -2**31 or result > 2**31 - 1:
    #         return 0
    #     return result

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        abs_x = abs(x)
        reversed = 0
        while abs_x > 0:
            reversed = reversed * 10 + abs_x % 10
            abs_x = abs_x // 10

        if reversed < -2**31 or reversed > 2**31 - 1:
            return 0
        return reversed * sign


solution = Solution()
print(solution.reverse(-1232))
