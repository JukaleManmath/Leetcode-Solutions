class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split("/")
        print(arr)

        for i in arr:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        res = "/"
        for i in stack:
            res = res + i + "/"
        return res[:-1] if len(res) > 1 else res
