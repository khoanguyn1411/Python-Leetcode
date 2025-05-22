# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         x = abs(x)

#         # Convert number to list of digits
#         digits = [int(d) for d in str(x)]

#         left, right = 0, len(digits) - 1

#         while right >= left:
#             if digits[left] == digits[right]:
#                 left, right = left + 1, right - 1
#             else:
#                 return False
#         return True


# solution = Solution()
# print(solution.isPalindrome(10))


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False

#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = x % 10 + reversed_half * 10
#             x = x // 10

#         return x == reversed_half or x == reversed_half // 10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_x = 0
        while reversed_x < x:
            reversed_x = reversed_x * 10 + x % 10
            if reversed_x != x:
                x = x // 10
        return reversed_x == x


solution = Solution()
print(solution.isPalindrome(1))
