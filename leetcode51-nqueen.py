from typing import List


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         result = []

#         def backtrack(combo: List, remain_q):
#             if remain_q == 0:
#                 result.append(combo.copy())
#             for j in range(n):
#                 chess_cell = ""
#                 for _ in range(n):
#                     chess_cell += "."
#                 chess_cell = chess_cell[:j] + "Q" + chess_cell[j+1:]
#                 should_continue = True
#                 for i in range(len(combo)):
#                     if chess_cell == combo[i]:
#                         should_continue = False
#                         break
#                     left_corner = j - (len(combo) - i)
#                     right_corner = j + (len(combo) - i)
#                     if left_corner >= 0 and combo[i][left_corner] == "Q":
#                         should_continue = False
#                         break
#                     if right_corner < n and combo[i][right_corner] == "Q":
#                         should_continue = False
#                         break
#                 if not should_continue:
#                     continue
#                 combo.append(chess_cell)
#                 backtrack(combo, remain_q - 1)
#                 combo.pop()

#         backtrack([], n)
#         return result


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(combo: List[str], row: int, cols: set, diag1: set, diag2: set):
            if row == n:
                result.append(combo.copy())
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                row_str = "." * col + "Q" + "." * (n - col - 1)
                combo.append(row_str)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(combo, row + 1, cols, diag1, diag2)

                combo.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack([], 0, set(), set(), set())
        return result


solution = Solution()
print(solution.solveNQueens(4))
