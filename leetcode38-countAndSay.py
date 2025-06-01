class Solution:
    def countAndSay(self, n: int) -> str:
        def recurse(next, i_term):

            if i_term == n:
                return next
            else:
                next_term = ""
                k = len(next)
                count = 1
                for i in range(0, k):
                    if i == k - 1:
                        next_term += str(count) + next[i]
                    elif i < k and next[i] == next[i + 1]:
                        count += 1
                    else:
                        next_term += str(count) + next[i]
                        count = 1
                return recurse(next_term, i_term + 1)

        return recurse("1", 1)


solution = Solution()
print(solution.countAndSay(4))
