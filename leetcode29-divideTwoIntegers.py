# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31

#         # Handle overflow case
#         if dividend == INT_MIN and divisor == -1:
#             return INT_MAX

#         # Determine the sign of the result
#         negative = (dividend < 0) != (divisor < 0)

#         # Work with absolute values
#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         quotient = 0

#         # Subtract divisor multiples using bit shifts
#         while dividend >= divisor:
#             temp = divisor
#             multiple = 1
#             while dividend >= (temp << 1):
#                 temp <<= 1
#                 multiple <<= 1

#             dividend -= temp
#             quotient += multiple
#             print(dividend, quotient)

#         return -quotient if negative else quotient


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        multiply = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            total_divisor = divisor
            multiply = 1
            while dividend > total_divisor * 2:
                total_divisor = total_divisor * 2
                multiply = multiply * 2
            quotient += multiply
            dividend -= total_divisor

        return -quotient if negative else quotient


solution = Solution()
print(solution.divide(10, 3))
