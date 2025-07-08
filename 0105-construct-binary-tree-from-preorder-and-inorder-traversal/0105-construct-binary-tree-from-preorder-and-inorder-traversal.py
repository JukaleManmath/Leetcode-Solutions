# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = preorder.pop(0)
        root_idx = 0
        for i in range(len(inorder)):
            if inorder[i] == root:
                root_idx = i
                break
        
        left_subtree = [inorder[i] for i in range(root_idx)]
        right_subtree = [inorder[i] for i in range(root_idx+1, len(inorder))]
        root  = TreeNode(root)
        root.left = self.buildTree(preorder, left_subtree) if left_subtree else None
        root.right = self.buildTree(preorder, right_subtree) if right_subtree else None

        return root
        
        


        