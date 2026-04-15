# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        tree = []
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr:
                tree.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                tree.append("null")
        return ",".join(tree)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        tree = data.split(",")

        root = TreeNode(int(tree[0]))

        q = deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if tree[i] != "null":
                curr.left = TreeNode(int(tree[i]))
                q.append(curr.left)
            i += 1

            if tree[i] != "null":
                curr.right = TreeNode(int(tree[i]))
                q.append(curr.right)
            i += 1
        return root
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans