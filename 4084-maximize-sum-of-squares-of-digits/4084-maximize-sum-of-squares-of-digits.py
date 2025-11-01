class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ""
        while num:
            val = "9" if sum - 9 >= 0 else str(sum)
            ans += val
            sum -= int(val)
            num -= 1
        
        if sum:
            return ""
        return ans
            
            
        