# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to handle edge cases easily
        dummy.next = head
        prev = dummy  # Previous node starts at dummy
        current = head  # Current node starts at head
        
        while current:
            # Move to the last occurrence of a duplicated number
            while current.next and current.val == current.next.val:
                current = current.next
            # If prev.next is current, no duplicates were found
            if prev.next == current:
                prev = prev.next
            else:
                # Skip all duplicates
                prev.next = current.next
            # Move to the next node
            current = current.next
        
        return dummy.next

# Runtime Complexity: O(n)
# Space Complexity: O(1)