class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if tokens[i] == "+":
                    ans = (num2 + num1)
                elif tokens[i] == "-":
                    ans = (num2 - num1)
                elif tokens[i] == "*":
                    ans = (num2 * num1)
                else:
                    ans = (num2 / num1)
                stack.append(ans)
            else:
                stack.append(tokens[i])
        
        return int(stack.pop())