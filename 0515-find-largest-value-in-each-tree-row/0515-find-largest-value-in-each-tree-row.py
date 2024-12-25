# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def bfs(node):
            ans= []
            q = deque([node])

            if not node:
                return []
            
            while(q):
                level = []
                max_element = float("-inf")
                for _ in range(len(q)):
                    n = q.popleft()
                    max_element = max(max_element, n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    
                ans.append(max_element)
            
            return ans
            

        return bfs(root)