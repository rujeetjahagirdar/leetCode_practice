# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = t1 = ListNode()
        head2 = t2 = ListNode()

        current = head

        while(current):
            if(current.val<x):
                t1.next = ListNode(current.val)
                t1 = t1.next
            else:
                t2.next = ListNode(current.val)
                t2 = t2.next
            current=current.next
        t1.next = head2.next

        return head1.next