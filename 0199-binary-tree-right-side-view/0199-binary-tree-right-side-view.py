# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        #bfs,
        ans = []

        q = deque()

        q.append(root)

        while(q):
            levelLenght = len(q)
            for i in range(levelLenght):
                n = q.popleft()
                if(i==levelLenght-1):
                    ans.append(n.val)
                
                if(n.left):
                    q.append(n.left)
                if(n.right):
                    q.append(n.right)
        
        return(ans)