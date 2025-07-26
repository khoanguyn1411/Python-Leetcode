from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result: List[List[int]] = []
        for _ in range(n):
            result.append([])
        for re in result:
            for _ in range(n):
                re.append(0)

        left, right = 0, n
        top, bottom = 0, n
        current_index = 1
        while left < right and top < bottom:
            # left -> right
            for i in range(left, right):
                result[top][i] = current_index
                current_index += 1
            top += 1

            # top -> bottom
            for i in range(top, bottom):
                result[i][right - 1] = current_index
                current_index += 1
            right -= 1

            if not (left < right and top < bottom):
                return result

            # right -> left
            for i in range(right - 1, left - 1, -1):
                result[bottom - 1][i] = current_index
                current_index += 1

            bottom -= 1

            # bottom -> top
            for i in range(bottom - 1, top - 1, -1):
                result[i][left] = current_index
                current_index += 1

            left += 1

        return result


print(Solution().generateMatrix(3))
