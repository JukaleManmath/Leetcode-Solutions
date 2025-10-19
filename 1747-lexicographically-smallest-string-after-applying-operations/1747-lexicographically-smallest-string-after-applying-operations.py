class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = [s]
        q = deque([s])

        def operation(n1):
            add = ""
            rotate = ""
            for i in range(len(n1)):
                if i % 2 != 0:
                    add += str((int(n1[i])+ a) % 10)
                else:
                    add += n1[i]
            rotate = n1[b:] + n1[:b]
            return [add, rotate]
        while q:
            n = len(q)
            for i in range(n):
                n1 = q.popleft()
                add, rotate = operation(n1)
    
                if add not in seen:
                    seen.append(add)
                    q.append(add)

                if rotate not in seen:
                    seen.append(rotate)
                    q.append(rotate)
        return min(seen)

