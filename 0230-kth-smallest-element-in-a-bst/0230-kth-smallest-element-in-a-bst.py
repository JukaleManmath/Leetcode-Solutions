# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS- naive approach O(nlogn) - due to sorting
        # def dfs(root, res):
        #     if not root:
        #         return res
        #     res.append(root.val)

        #     if root.left:
        #         res = dfs(root.left, res)
        #     if root.right:
        #         res = dfs(root.right, res)
            
        #     return res
        # res = dfs(root, [])
        # res.sort()
        # return res[k-1]

        # using in inorder we can skip the sorting part left -> root -> right it is already a sorted sequence
        arr = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return arr[k-1]