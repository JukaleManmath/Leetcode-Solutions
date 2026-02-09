# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        arr.sort()

        def createBST(arr, start, end):
            if start > end:
                return None
            mid = start + (end - start)//2
            lefttree = createBST(arr, start, mid - 1)
            righttree = createBST(arr, mid + 1, end)

            root = TreeNode(arr[mid], lefttree, righttree)
            return root
        return createBST(arr,0 , len(arr) - 1)
        
        