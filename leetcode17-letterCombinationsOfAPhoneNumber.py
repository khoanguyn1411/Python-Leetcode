from typing import List


phone_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if not digits:
            return combinations

        def recursion(combination, i_number):
            if i_number == len(digits):
                combinations.append(combination)
                return
            for char in phone_map[digits[i_number]]:
                recursion(combination + char, i_number + 1)

        recursion("", 0)
        return combinations


solution = Solution()
print(solution.letterCombinations("23"))
