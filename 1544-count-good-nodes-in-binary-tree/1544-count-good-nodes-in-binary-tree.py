# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        # mxTillNow = root.val
        stack = [(root, root.val)]
        ans=0

        while stack:
            n, mxTillNow = stack.pop()

            if(n.val>=mxTillNow):
                ans+=1
                mxTillNow = max(mxTillNow, n.val)
            
            if(n.right):
                stack.append((n.right, mxTillNow))
            
            if(n.left):
                stack.append((n.left, mxTillNow))

            # print(stack)
            print(mxTillNow)
            print("ans= ",ans)
        return ans