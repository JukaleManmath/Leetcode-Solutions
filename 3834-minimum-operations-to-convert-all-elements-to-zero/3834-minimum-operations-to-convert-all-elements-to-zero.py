class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # this is a montonic stack problem (increasing value stack ) keep attention to the values increasing and descreasing.
        # according to question we are going to go from smallest -> largest and this approach will replace what will smallest removal lead in the way with 100% surity (look at the decision we made)
        
        stack = []
        res = 0

        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            
            if n > 0 and (not stack or n > stack[-1]):
                res += 1
                stack.append(n)
        
        return res