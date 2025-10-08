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
        p_path = []

        curr = p

        while(curr):
            p_path.append(curr)
            curr = curr.parent
        
        print(p_path)

        q_path = []

        curr= q

        while(curr):
            q_path.append(curr)
            curr = curr.parent
        
        print(q_path)

        for i in p_path:
            if(i in q_path):
                return i