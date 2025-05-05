# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = curr = ListNode(-1)

        remainder = 0

        while l1 or l2:
            if(l1 and l2):
                sm = (l1.val + l2.val) + remainder
                remainder = sm//10
                curr.next = ListNode(sm%10)

                l1 = l1.next
                l2 = l2.next
            elif(l1 and not l2):
                sm = (l1.val +0) + remainder
                remainder = sm//10
                curr.next = ListNode(sm%10)
                l1 = l1.next
            elif(not l1 and l2):
                sm = (0 + l2.val) + remainder
                remainder = sm//10
                curr.next = ListNode(sm%10)
                l2 = l2.next
            curr = curr.next
        
        if(remainder>0):
            curr.next = ListNode(remainder)
        return(dummy.next)
