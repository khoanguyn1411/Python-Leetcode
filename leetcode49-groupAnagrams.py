from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in dict:
                dict[sorted_str] = [str]
            else:
                dict[sorted_str].append(str)
        return list(dict.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
