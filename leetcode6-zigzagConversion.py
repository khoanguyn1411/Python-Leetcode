class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        char_index = {}

        for i in range(1, numRows + 1):
            char_index[i] = ""

        current_index = 1
        is_increase = True

        for char in s:

            char_index[current_index] += char

            if is_increase:
                current_index += 1
            else:
                current_index -= 1

            if current_index == 1:
                is_increase = True
            elif current_index == numRows:
                is_increase = False

        return "".join(char_index.values())


solution = Solution()
print(solution.convert("PAYPALISHIRING", 4))
