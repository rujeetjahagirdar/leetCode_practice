"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        #three cases
            #case 1 can be inserted in betwenn linked list
            #cse2 need to insert at end of list after last element of the list
            #case 3: all elements equal of list, insert at anywhere
        #use two pointer

        #NOTE: Head would be anywhere in the list, not necesossrly at lowest element

        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode

            return newNode

        curr = head
        forward = head.next

        while(forward!=head):
            if(curr.val<=insertVal<=forward.val):
                newNode = Node(insertVal)
                newNode.next = forward
                curr.next = newNode

                break
            
            if(curr.val>forward.val): #wrap around location 
                if(insertVal>=curr.val or insertVal<=forward.val):
                    newNode = Node(insertVal)
                    newNode.next = forward
                    curr.next = newNode

                    break
            
            curr = curr.next
            forward = forward.next
        
        #if we could not find location

        newNode = Node(insertVal)
        newNode.next = forward
        curr.next = newNode

        return head