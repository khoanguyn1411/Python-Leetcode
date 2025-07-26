class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        return len(stripped.split(" ")[-1])


print(Solution().lengthOfLastWord("Hello World"))
