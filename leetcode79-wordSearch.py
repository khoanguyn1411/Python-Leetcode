from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board[0]), len(board)

        def backtrack(pos_search, search_index):
            x = pos_search["x"]
            y = pos_search["y"]

            if search_index == len(word):
                return True

            if y >= n or x >= m or y < 0 or x < 0:
                return False

            current_value = board[y][x]

            if current_value == word[search_index]:
                new_search_index = search_index + 1
                temp = board[y][x]
                board[y][x] = "#"

                cases = [{"x": x + 1, "y": y}, {"x": x, "y": y + 1},
                         {"x": x - 1, "y": y}, {"x": x, "y": y - 1}]

                result = []

                for case in cases:
                    new_x = case["x"]
                    new_y = case["y"]
                    is_result = backtrack(
                        {"x": new_x, "y": new_y}, new_search_index)

                    result.append(is_result)
                board[y][x] = temp
                return True in result

            return False

        for i in range(m):
            for j in range(n):
                if backtrack({"x": i, "y": j}, 0):
                    return True

        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]], "ABCCED")
      )
