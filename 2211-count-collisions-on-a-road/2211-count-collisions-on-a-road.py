class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = [directions[0]]
        collisions= 0
        n = len(directions)
        for i in range(1, n):
            if stack[-1] == "R" and (directions[i] == "S" or directions[i] == "L"):
                stack.pop()
                collisions += 2 if directions[i] == "L" else 1
                while stack and stack[-1] == "R":
                    stack.pop()
                    collisions += 1
                    
                stack.append("S")
            elif directions[i] == "L" and stack[-1] == "S":
                collisions  += 1
            elif directions[i] == "S":
                stack = ["S"]
            else:
                stack.append(directions[i])
            
        return collisions      