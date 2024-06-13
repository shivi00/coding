# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r):
            if r:
                l=dfs(r.left)
                r=dfs(r.right)
                return 1+max(l,r)
            else:
                return 0
        return dfs(root)