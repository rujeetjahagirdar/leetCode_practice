# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans=[]

        colElements = defaultdict(list)

        q = deque()
        q.append((root, 0, 0))

        while q:
            for _ in range(len(q)):
                n, row, col = q.popleft()

                colElements[col].append((n.val, row))

                if(n.left):
                    q.append((n.left, row+1, col-1))
                
                if(n.right):
                    q.append((n.right, row+1, col+1))
        
        print(colElements)

        sorted_key = sorted(colElements.keys())

        for key in sorted_key:
            t=[]
            for n in sorted(colElements[key], key=lambda x: (x[1], x[0])):
                t.append(n[0])
            ans.append(t)

        return(ans)