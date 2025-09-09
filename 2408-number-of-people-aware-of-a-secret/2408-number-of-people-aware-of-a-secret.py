class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        total = 1
        share = 0
        aware = [0] * n
        aware[0] = 1

        for i in range(1, n):
            if i >= delay:
                share += aware[i - delay]
            if i >= forget:
                total -= aware[i- forget]
                share -= aware[i - forget]
            aware[i] = share
            total += share
            
        return total % (10 **9 + 7)
