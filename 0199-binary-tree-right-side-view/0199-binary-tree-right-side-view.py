# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []
        if not root:
            return []
        q.append(root)
        while q:
            # rightNode = None
            qLen = len(q)
            for i in range(qLen):
                n = q.popleft()
                if n:
                    # rightNode = n
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
            ans.append(n.val) 
        print(ans)
        return ans