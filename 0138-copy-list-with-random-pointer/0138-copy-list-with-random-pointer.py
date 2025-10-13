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
        
        #make dummy node for new list
        #maintain visited hash map
        #use two passes
            #first: parse original list and fill only next pointers for new list
            #second: now fill random pointers


        visited_mapping = {}

        dummy = newPtr = Node(-1)

        curr = head

        #first pass
        while curr:
            newNode = Node(curr.val, curr.next)

            visited_mapping[curr] = newNode

            newPtr.next = newNode
            newPtr = newPtr.next

            curr = curr.next
        
        #second pass
        curr = head

        while curr:
            if(curr.random==None):
                visited_mapping[curr].random = None
            else:
                visited_mapping[curr].random = visited_mapping[curr.random]
            
            curr = curr.next
        
        return dummy.next
        
            