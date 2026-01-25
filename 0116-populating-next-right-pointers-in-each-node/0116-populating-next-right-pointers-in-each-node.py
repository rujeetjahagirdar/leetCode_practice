"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        
        def bfs(node):
            q = deque([node])
            # print(len(q))
            # print(q[0])
            while(q):
                # prev = None
                levelNode=[]
                for i in range(len(q)):
                    n = q.popleft()
                    levelNode.append(n)
                    # if(prev!=None):
                    #     prev.next = n
                    # prev=n
                    
                    if(n.left):
                        q.append(n.left)
                    if(n.right):
                        q.append(n.right)
                
                # print(levelNode)
                for i in range(len(levelNode)-1):
                    levelNode[i].next = levelNode[i+1]

            # print(root)
            return 
        
        bfs(root)
        return root