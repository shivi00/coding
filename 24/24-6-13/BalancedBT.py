# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                l=dfs(root.left)
                r=dfs(root.right)
                if abs(l[0]-r[0])<=1 and l[1]==True and r[1]==True:
                    return [1+max(l[0],r[0]),True]
                else:
                    return [1+max(l[0],r[0]),False]
            else:
                return [0,True]
        return dfs(root)[1]
        