class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i == "+":
                b = res.pop()
                a = res.pop()
                res.append(a + b)
            elif i == "-":
                b = res.pop()
                a = res.pop()
                res.append(a - b)
            elif i == "*":
                b = res.pop()
                a = res.pop()
                res.append(a * b)
            elif i == "/":
                b = res.pop()
                a = res.pop()
                res.append(int(a / b))
            else:
                res.append(int(i))

        return res[0]