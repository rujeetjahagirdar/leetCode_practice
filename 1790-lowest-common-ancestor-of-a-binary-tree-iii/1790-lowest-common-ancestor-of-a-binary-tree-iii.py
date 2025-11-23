"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        #trace path for any one node
        #while tracing for other node, check if it exists in path for previous node

        #TC: O(n)
        #SC: O(n)

        p_path = []

        curr = p

        while(curr):
            p_path.append(curr)
            curr = curr.parent
        
        curr = q

        while(curr):
            if(curr in p_path):
                return curr
            curr = curr.parent
        
        return None
    
