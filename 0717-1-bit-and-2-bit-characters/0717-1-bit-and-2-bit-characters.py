class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1 and bits[-1] == 0:
            return True

        n = len(bits)
        i = 0
        while i < n:
            if bits[i] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1
            
            if i == n -1:
                return True
        return False