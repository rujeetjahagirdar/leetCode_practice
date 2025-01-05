# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        prev, curr = dummyNode, head


        if not head:
            return
        
        while(curr):
            if(curr.val==val):
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        print(dummyNode)
        return dummyNode.next

