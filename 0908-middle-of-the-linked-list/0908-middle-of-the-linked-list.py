# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        node_count=0

        while(curr):
            node_count+=1
            curr = curr.next
        
        print(node_count)

        curr = head

        for _ in range(node_count//2):
            curr = curr.next
        
        return curr