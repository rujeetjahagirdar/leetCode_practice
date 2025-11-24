"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
        
        old_to_new_node = {}
        curr = head
        dummy = headNew = Node(-1)

        while(curr):
            newNode = Node(x=curr.val, next=curr.next, random=None)
            headNew.next = newNode
            old_to_new_node[curr] = newNode

            headNew = headNew.next
            curr = curr.next

        
        print(dummy.next.val)

        curr = head
        while(curr):
            if(curr.random):
                old_to_new_node[curr].random = old_to_new_node[curr.random]
            # else:
            #     old_to_new_node[curr].random = None
            
            curr = curr.next
        
        return dummy.next

