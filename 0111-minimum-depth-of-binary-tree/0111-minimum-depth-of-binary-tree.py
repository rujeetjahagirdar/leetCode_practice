# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        #bfs

        ans=0

        q = deque([root])

        while(q):
            #process queue level wise
            
            ans+=1

            # print(n)

            for _ in range(len(q)):
                n = q.popleft()

                if(not n.left and not n.right):
                    return ans
                
                if(n.left):
                    q.append(n.left)
                
                if(n.right):
                    q.append(n.right)
        