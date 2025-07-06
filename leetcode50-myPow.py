# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1

#         if n < 0:
#             x = 1/x

#         n = abs(n)
#         total = 1
#         total_in_loop = x
#         up_n = 1
#         while n > 0:
#             up_n = up_n * 2
#             total_in_loop = total_in_loop * total_in_loop if n > 1 else total_in_loop
#             if up_n * 2 > n:
#                 total *= total_in_loop
#                 total_in_loop = x
#                 n = n - up_n
#                 up_n = 1
#         return total


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2

        return result


solution = Solution()
print(solution.myPow(2, -2))
