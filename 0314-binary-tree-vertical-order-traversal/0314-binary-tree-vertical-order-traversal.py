# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        columnHash = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            n, col = q.popleft()

            columnHash[col].append(n.val)

            if(n.left):
                q.append((n.left, col-1))
            if(n.right):
                q.append((n.right, col+1))
        
        print(columnHash)
        l=sorted(columnHash.keys())
        print(l)
        ans=[columnHash[i] for i in l]
        return ans