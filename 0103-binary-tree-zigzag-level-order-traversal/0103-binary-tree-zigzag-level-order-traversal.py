# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        ans=[]

        def bfs(node):
            q = deque([root])
            reverse=False
            while q:
                t= []

                for _ in range(len(q)):
                    n = q.popleft()
                    if(n):
                        t.append(n.val)
                    if(n.left):
                        q.append(n.left)
                    if(n.right):
                        q.append(n.right)
                if(reverse):
                    ans.append(t[::-1])
                    reverse=False
                else:
                    ans.append(t)
                    reverse=True



        bfs(root)
        print(ans)
        return ans