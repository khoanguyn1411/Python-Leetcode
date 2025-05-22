from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        max_loop = min(len(s) for s in strs)

        for i in range(max_loop):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return common_prefix
            common_prefix += char

        return common_prefix


solution = Solution()
print(solution.longestCommonPrefix(["cir", "car"]))
