# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maximum_value
        maximum_value=[0]
        def dfs(root):
            if root:
                l=dfs(root.left)
                r=dfs(root.right)
                if l+r+2> maximum_value[0]:
                     maximum_value[0]= l+r+2
                return 1+max(l,r)
            else:
                return -1
        dfs(root)
        return  maximum_value[0]