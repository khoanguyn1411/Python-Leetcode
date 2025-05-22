class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     row_dic = {}
    #     for i in range(numRows):
    #         row_dic[i + 1] = []
    #     char_real_position = 1
    #     is_increase = True

    #     if numRows == 1 or numRows >= len(s):
    #         return s

    #     for i, char in enumerate(s):

    #         row_dic[char_real_position].append(char)

    #         if is_increase:
    #             char_real_position = char_real_position + 1
    #         else:
    #             char_real_position = char_real_position - 1

    #         if char_real_position == numRows or char_real_position == 1:
    #             is_increase = not is_increase

    #     char_arr = row_dic.values()
    #     result = ""
    #     for sub_arr in char_arr:
    #         for char in sub_arr:
    #             result = "".join([result, char])
    #     return result

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_dic = {}
        for i in range(numRows):
            row_dic[i + 1] = ""
        position = 1
        is_increase = True
        for i, char in enumerate(s):
            if position == 1:
                is_increase = True
            if position == numRows:
                is_increase = False
            row_dic[position] = row_dic[position] + char

            if is_increase:
                position += 1
            else:
                position -= 1
        new_str = ""
        for val in row_dic.values():
            new_str += val
        return new_str


solution = Solution()
print(solution.convert("PAYPALISHIRING", 4))
