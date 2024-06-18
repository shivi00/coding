from collections import deque
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
        pre=[]
        def dfs(root):
            if root:
                pre.append(root.val)
                dfs(root.left)
                dfs(root.right)
            else:
                pre.append("N")
        
        dfs(root)
        return ",".join(str(e) for e in pre)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pre=[]
        pre= data.split(",")
        n=len(pre)
        for i in range(n):
            if pre[i]!="N":
                pre[i]=int(pre[i])
        
        
        def createTree(pre):
            if pre[0]=="N":
                pre.pop(0)
                return None
            root=TreeNode(pre.pop(0))
            root.left = createTree(pre)
            root.right = createTree(pre)
            return root
        
        return createTree(pre)