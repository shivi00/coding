
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,l,g):
            if not root:
                return True
            if l>=root.val or root.val>=g :
                return False
            return dfs(root.left,l,root.val) and dfs(root.right,root.val,g)
        return dfs(root,float('-inf'),float('inf'))
            