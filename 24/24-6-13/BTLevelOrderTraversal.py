from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        res=[]
        while len(q):
            k=len(q)
            temp=[]
            while k!=0:
                n=q.popleft()
                
                if n.left!=None:
                    q.append(n.left)
                if n.right!=None:
                    q.append(n.right)
                temp.append(n.val)
                k-=1
            res.append(temp)
                
        return res
        