# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans=[]

        def bfs(node):
            q = deque([node])
            sm=0

            while q:
                sm=0
                cnt = len(q)
                for _ in range(len(q)):
                    n = q.popleft()
                    if(n):
                        sm+=n.val
                    if(n.left):
                        q.append(n.left)
                    if(n.right):
                        q.append(n.right)
                ans.append(sm/cnt)
        bfs(root)
        return(ans)