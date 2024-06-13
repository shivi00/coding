# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r=root
        def dfs(r):
            if r:
                t=r.left
                r.left=r.right
                r.right=t
                dfs(r.left)
                dfs(r.right)
        dfs(r)
        return root