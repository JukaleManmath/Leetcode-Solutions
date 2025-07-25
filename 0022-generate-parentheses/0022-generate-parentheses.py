class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(s, open_cts, close_cts, arr):
            if len(s) == 2 * n and open_cts == close_cts:
                arr.append(s)
            
            if open_cts < n:
                recursion(s+ "(", open_cts+1, close_cts, arr)
            if close_cts < open_cts:
                recursion(s+ ")", open_cts, close_cts+1, arr)
            return arr
        res = recursion("", 0, 0 , [])
        return res