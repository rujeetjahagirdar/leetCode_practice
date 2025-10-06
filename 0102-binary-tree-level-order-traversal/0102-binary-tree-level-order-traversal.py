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

        q = deque([root])

        while q:
            # print(q)
            t = []
            for i in range(len(q)):
                
                n = q.popleft()
                # print(n.val)
                t.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                
            ans.append(t)
        
        return(ans)