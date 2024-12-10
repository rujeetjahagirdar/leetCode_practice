# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]

        if not root:
            return []

        def bfs(node):
            q = deque([node])

            while q:
                t = []
                for _ in range(len(q)):
                    n = q.popleft()
                    if(n):
                        t.append(n.val)
                    if(n.left):
                        q.append(n.left)
                    if(n.right):
                        q.append(n.right)
                ans.append(t)
        
        bfs(root)
        print(ans)
        return ans