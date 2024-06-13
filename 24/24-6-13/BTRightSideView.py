# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        res=[]
        while len(q):
            k=len(q)
            while k!=0:
                n=q.popleft()
                if n.left!=None:
                    q.append(n.left)
                if n.right!=None:
                    q.append(n.right)
                if k==1:
                    res.append(n.val)
                k-=1
        return res