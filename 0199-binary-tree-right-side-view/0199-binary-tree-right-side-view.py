# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #bfs, top down

        ans=[]

        def bfs(node):
            
            q = deque()
            q.append(node)

            while q:
                qlen = len(q)
                for i in range(len(q)):
                    
                    n = q.popleft()
                    if(i==qlen-1):
                        ans.append(n.val)
                    
                    if(n.left):
                        q.append(n.left)
                    
                    if(n.right):
                        q.append(n.right)
            
        
        if not root:
            return []

        bfs(root)
        return(ans)
