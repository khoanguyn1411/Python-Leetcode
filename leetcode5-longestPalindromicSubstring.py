class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expandAroundCenter(i, i)
            # Even length palindrome
            even = expandAroundCenter(i, i + 1)
            # Pick the longer one
            current_longest = odd if len(odd) > len(even) else even
            if len(current_longest) > len(longest):
                longest = current_longest

        return longest


solution = Solution()
print(solution.longestPalindrome("ab"))
