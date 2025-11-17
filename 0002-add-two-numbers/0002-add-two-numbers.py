# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(max(m, n))
        #SC: O(1)
        
        carry = 0
        head = curr = ListNode(-1)

        if(not l1):
            return l2
        
        if(not l2):
            return l1

        while(l1 or l2):
            if(l1):
                n1 = l1.val
            else:
                n1 = 0

            if(l2):
                n2 = l2.val
            else:
                n2=0
            
            sm = (n1+n2)+carry

            curr.next = (ListNode(sm%10))

            carry = (sm)//10

            if(l1):
                l1 = l1.next
            else:
                l1=None
            
            if(l2):
                l2 = l2.next
            else:
                l2 = None
            
            curr = curr.next
        
        if(carry>0):
            curr.next = ListNode(carry)
            carry = 0

        return head.next
