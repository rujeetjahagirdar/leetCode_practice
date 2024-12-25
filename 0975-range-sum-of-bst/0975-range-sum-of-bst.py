# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        if not root:
            return

        q = deque([root])

        while(q):

            for _ in range(len(q)):
                n = q.popleft()
                if(n.val>=low and n.val<=high):
                    ans+=n.val
                
                if n.left:
                    q.append(n.left)
                
                if n.right:
                    q.append(n.right)
                
            print(ans)
        return ans