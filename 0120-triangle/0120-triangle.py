class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        path = {}

        def dfs(i , level):
            if level == n -1:
                return triangle[level][i]
            if (i,level) in path:
                return path[(i,level)]
            
            path[(i,level)]= min(triangle[level][i] + dfs(i , level + 1),
                        triangle[level][i] + dfs(i + 1 , level + 1))
            return path[(i,level)]
        
        return dfs(0,0)