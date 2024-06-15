# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[root]
        ans=[]
        while len(stack):
            while stack[-1].left!=None:
                stack.append(stack[-1].left)
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
                continue
            else:
                if len(stack):
                    stack[-1].left=None
        return ans[k-1]