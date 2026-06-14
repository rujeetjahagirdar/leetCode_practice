# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []

        while(head):
            values.append(head.val)
            head = head.next
        
        print(values)

        ans=0

        for i in range(len(values)//2):
            sm = values[i] + values[-(i+1)]
            ans = max(ans, sm)
        
        print(ans)

        return ans