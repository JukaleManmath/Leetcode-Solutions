class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = [False] * len(fruits)
        n = len(fruits)
        l , r = 0 , 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j] and not placed[j]:
                    placed[j] = True
                    break
        
        cnt = 0
        for c in placed:
            if c == False:
                cnt += 1
        return cnt

