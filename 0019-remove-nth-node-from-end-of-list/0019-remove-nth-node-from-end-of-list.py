# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # p1=head
        # p2=head
        # values=[]
        # while p1:
        #     values.append(p1.val)
        #     p1=p1.next
        # nval = values[-n]
        # prev, curr = None, p2
        # while(curr):
        #     if(curr.val==nval):
        #         if prev:
        #             prev.next = curr.next
        #         else:
        #             head=curr.next
        #     prev=curr
        #     curr=curr.next
        # # print(head)
        # return head
        left, right = head, head
        for _ in range(n):
            right = right.next
        # print(left.val)
        # print(right.val)
        while(right and right.next):
            left = left.next
            right=right.next
        # print(left.val)
        # print(right.val)
        if(n==1):
            if(left.next):
                left.next=None
            else:
                head=None
        else:
            if(right):
                left.next=left.next.next
            else:
                head = left.next
        return(head)
            