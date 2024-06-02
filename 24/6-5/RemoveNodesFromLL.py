# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,nxt=head,head.next
        v=[prev]
        while nxt:
            if prev.val>nxt.val:
                v.append(nxt)
            else:
                j=-1
                while len(v):
                    if v[-1].val<nxt.val:
                        v.pop()
                    else:
                        break
                v.append(nxt)
                
            prev=prev.next
            nxt=nxt.next
        n=len(v)
        for i in range(n-1):
            v[i].next=v[i+1]
        return v[0]