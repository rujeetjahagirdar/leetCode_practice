# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans=0
        digits = []
        while head:
            digits.append(head.val)
            head = head.next
        
        print(digits)

        n = len(digits)

        for i in digits:
            # print(i, n-1)
            ans+=i*(2**(n-1))
            # print(ans)
            n-=1
        return ans