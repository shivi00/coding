# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, h):
        prev=None
        curr=h
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        q=self.rev(h)
        h=q
        c=0
        while h:
            s=((h.val*2)%10)+c
            c=((h.val*2)//10)
            h.val=s
            if c!=0 and h.next==None:
                h.next=ListNode(c,None)
                break
            h=h.next
            
        
        return self.rev(q)