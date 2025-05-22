class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def check_match(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            is_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return (check_match(i, j + 2)  # use the "*", move j by 2.
                        or (is_match and check_match(i + 1, j)))  # not use the "*", keep j, move i by 1.
            if is_match:
                return check_match(i + 1, j + 1)

            return False
        return check_match(0, 0)


solution = Solution()
print(solution.isMatch("ab", "ab*"))
