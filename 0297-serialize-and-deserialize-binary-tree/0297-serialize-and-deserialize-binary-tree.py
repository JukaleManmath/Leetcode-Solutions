# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return
            root = TreeNode(vals[self.i])
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))