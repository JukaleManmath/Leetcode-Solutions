class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        groups = defaultdict(list)
        for x, y, t in meetings:
            groups[t].append((x, y))
        
        can = {0 , firstPerson}
        for _ , val in sorted(groups.items()):
            current_groups = defaultdict(list)
            current_stack = set()

            for x, y in val:
                current_groups[x].append(y)
                current_groups[y].append(x)
                if x in can: current_stack.add(x)
                if y in can: current_stack.add(y)
            
            current_stack = list(current_stack)
            while current_stack:
                node = current_stack.pop()
                for nei in current_groups[node]:
                    if nei not in can:
                        can.add(nei)
                        current_stack.append(nei)
        return list(can)
