class Solution:
    def simplifyPath(self, path: str) -> str:
        arr_paths = path.split("/")
        stack = []
        for data in arr_paths:
            if data == "" or data == ".":
                continue
            if data != ".." or len(stack) == 0:
                stack.append(data)
                continue
            if stack:
                stack.pop()
                continue

        if not stack or stack[-1] == "..":
            return "/"

        if stack[0] == "..":
            stack.remove("..")

        return '/' + "/".join(stack)


# print(Solution().simplifyPath("/home//foo/"))
print(Solution().simplifyPath("/./qvzVS/oBx/vIN///../lyLw////"))
# print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
# print(Solution().simplifyPath("/abc/..."))
