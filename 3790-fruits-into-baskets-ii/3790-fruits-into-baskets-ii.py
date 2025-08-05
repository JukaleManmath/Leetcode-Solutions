class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1
                    break
        
        cnt = 0
        for c in baskets:
            if c != -1:
                cnt += 1
        return cnt

