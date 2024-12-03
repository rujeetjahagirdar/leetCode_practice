# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = ListNode(next=head), head
        ans=prev
        
        while(curr):
            if(curr.next and curr.next.val==curr.val):
                while(curr.next and curr.next.val==curr.val):
                    curr = curr.next
                prev.next = curr.next
                curr.next=None
                curr=prev
            else:
                prev = prev.next
            curr=curr.next
        
        return(ans.next)
