class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        seen = set()
        q = deque(initialBoxes)
        nokey = set()
        total = 0
        while q:
            curr = q.popleft()
            if curr in seen:
                continue
            
            if not status[curr]:
                nokey.add(curr)
                continue
            
            seen.add(curr)
            total += candies[curr]
            for i in containedBoxes[curr]:
                if i not in seen:
                    q.append(i)
            for i in keys[curr]:
                if i in nokey:
                    q.append(i)
                status[i] = 1
        return total


