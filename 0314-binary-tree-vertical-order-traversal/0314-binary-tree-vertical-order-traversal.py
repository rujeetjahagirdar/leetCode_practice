# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #bfs, top-down
        ans=[]
        result = defaultdict(list)
        
        def bfs(node):
            q = deque()
            q.append((node, 0)), #root node

            while q:
                for _ in range(len(q)):
                    n, col = q.popleft()
                    result[col].append(n.val)

                    if(n.left):
                        q.append((n.left, col-1))
                    if(n.right):
                        q.append((n.right, col+1))
            
        
        if not root:
            return []

        bfs(root)

        print(result)

        sorted_idx = sorted(result, key= lambda x: x)

        for idx in sorted_idx:
            ans.append(result[idx])
        
        return(ans)
