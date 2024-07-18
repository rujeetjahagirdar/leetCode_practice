# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        test = result
        remainder = 0
        while l1 or l2:
            # print(l1, l2, remainder)
            if(l1!=None and l2!=None):
                result.val = (l1.val + l2.val + remainder)%10 
                remainder = (l1.val + l2.val + remainder)//10
            elif(l1!=None and l2==None):
                result.val = (l1.val + 0+ remainder)%10
                remainder = (l1.val + 0 + remainder)//10
            elif(l2!=None and l1==None):
                result.val = (0 + l2.val + remainder)%10
                remainder = (0 + l2.val + remainder)//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            # remainder=0
            if l1!=None or l2!=None:
                result.next = ListNode()
                result=result.next
        if(remainder!=0):
            result.next=ListNode(remainder, None)
        return(test)