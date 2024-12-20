# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def bfs(root):
            if not root:
                return None
            
            q = deque([root])
            level=0

            while q:
                # node = q.popleft()
                current_level = []
                for _ in range(len(q)):
                    n = q.popleft()
                    current_level.append(n)
                    if(n.left):
                        q.append(n.left)
                    if(n.right):
                        q.append(n.right)
                
                if(level%2!=0):
                    left = 0
                    right = len(current_level)-1
                    while(left<right):
                        current_level[left].val, current_level[right].val = current_level[right].val, current_level[left].val
                        left+=1
                        right-=1

                level+=1
                    


        bfs(root)

        print(root)
        return root