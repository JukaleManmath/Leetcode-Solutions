# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # paths= []
        # def dfs(root, path):
        #     if root is None:
        #         return
            
        #     path.append(str(root.val))
        #     if root.left is None and root.right is None:
        #         paths.append("".join(path[:]))
        #     else:
        #         dfs(root.left, path )
        #         dfs(root.right, path)
        #     path.pop()
        # dfs(root,[])

        # res = 0
        # for b in paths:
        #     res += int(b, 2)
        # return res

        def dfs(node, path):
            if not node:
                return 0
            
            path = (path << 1) + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, 0)