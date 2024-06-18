# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx=[-100000000]
        def dfs(root):
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            maxx[0]=max(maxx[0], max(max(l,r)+root.val, max(l+r+root.val ,  root.val)))
            return  max(max(l,r)+root.val, root.val)
        dfs(root)
        return maxx[0]