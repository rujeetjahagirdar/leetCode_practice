# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return 
        if k==0 and not head:
            return
        if(not head.next):
            return head

        # 1. Get length of the linked list
        current = head
        length = 1
        while current.next:
            length+=1
            current=current.next
        old_tail = current  # save old tail for future use
        # print("Length of LL=", length)

        # 2. Get new end node newEnd th node will be new end node
        newEnd = length - (k % length)
        # print("endNode (nth node)= ",newEnd)

        # 3. Traverse to new end node
        count=1
        current = head
        while(count<newEnd and current.next):
            count+=1
            current=current.next
        
        # print("count= ", count)
        # print("head2= ", head2.val)

        # 4. chage linked list
        old_tail.next = head
        newHead = current.next
        current.next = None
        head = newHead 

        # print(head)
        return head
