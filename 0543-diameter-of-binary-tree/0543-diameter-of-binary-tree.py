# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #bottom up approach, dfs

        self.ans=0

        def findDiameter(node):
            if not node:
                return 0
            
            leftDepth = findDiameter(node.left)
            rightDepth = findDiameter(node.right)

            currentDiameter = leftDepth + rightDepth

            self.ans = max(self.ans, currentDiameter)

            return 1 + max(leftDepth, rightDepth)
        

        findDiameter(root)

        return self.ans