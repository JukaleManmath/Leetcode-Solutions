class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
    
    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isLeaf = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        row , col = len(board), len(board[0])
        res , visit = set() , set()

        def dfs(r, c , word, root):
            if r >= row or c >= col or r < 0 or c < 0 or board[r][c] not in root.children or (r , c)in visit:
                return
            visit.add((r,c))
            word += board[r][c]
            child = root.children[board[r][c]]
            if child.isLeaf:
                res.add(word)

            dfs(r + 1, c , word , child)
            dfs(r - 1, c , word , child)
            dfs(r , c + 1 , word , child)
            dfs(r , c - 1 , word , child)
            visit.remove((r, c))
        for r in range(row):
            for c in range(col):
                dfs(r ,  c, "", root)
        return list(res)