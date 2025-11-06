"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def traverse(curr):
            nonlocal prev, head
            if not curr:
                return
            
            traverse(curr.left)
            if(prev==None):
                prev = curr
                head = curr
                # return
            
            else:
                prev.right = curr
                curr.left = prev
                prev = curr

            traverse(curr.right)
        
        prev = None
        head = None

        if not root:
            return 

        traverse(root)
        # print(ans)

        prev.right = head
        head.left = prev

        return head