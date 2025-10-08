"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        if not head:
            n = Node(insertVal)
            n.next = n
            return n

        
        forward = head.next
        current = head

        while True:
            if(current.val<=insertVal<=forward.val):
                n = Node(insertVal, forward)
                current.next = n

                return head
            
            elif(forward.val<current.val):
                if(insertVal>=current.val or insertVal<=forward.val):
                    n = Node(insertVal, forward)
                    current.next = n

                    return head

            current = current.next
            forward = forward.next        

            if current==head:
                break
        
        #all nodes equal
        n = Node(insertVal, forward)
        current.next = n

        return head