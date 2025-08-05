class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = [False] * len(fruits)
        n = len(fruits)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j] and not placed[j]:
                    baskets[j] = -1
                    break
            else:
                cnt += 1
        
        return cnt

