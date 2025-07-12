from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
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
        return len(result)


solution = Solution()
print(solution.totalNQueens(4))
