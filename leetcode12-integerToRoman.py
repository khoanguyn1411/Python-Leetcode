hmap = {
    1:    'I',
    4:    'IV',
    5:    'V',
    9:    'IX',
    10:    'X',
    40:    'XL',
    50:    'L',
    90:    'XC',
    100:    'C',
    400:    'CD',
    500:    'D',
    900:    'CM',
    1000:    'M'
}


# class Solution:
#     def intToRoman(self, num: int) -> str:

#         def separate_number(num):
#             if num == 4 or num == 9:
#                 return [num]
#             if num >= 5:
#                 nums = [5]
#                 for i in range(num - 5):
#                     nums.append(1)
#                 return nums
#             else:
#                 nums = []
#                 for i in range(num):
#                     nums.append(1)
#                 return nums

#         first_num = "".join([hmap[number]
#                             for number in separate_number(num % 10)])
#         second_num = "".join([hmap[number * 10]
#                               for number in separate_number(num % 100 // 10)
#                               if num >= 10])
#         third_num = "".join([hmap[number * 100]
#                              for number in separate_number(num % 1000 // 100)
#                              if num >= 100])
#         four_num = "".join([hmap[1000]
#                            for _ in range(num // 1000) if num >= 1000])
#         return "".join([four_num, third_num, second_num, first_num])


class Solution:
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100,  90,  50,  40,
            10,   9,   5,   4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman


solution = Solution()
print(solution.intToRoman(1994))
