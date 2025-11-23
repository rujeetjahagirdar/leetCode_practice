# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        #dfs, top down
        #when leaf occurs, add number to gloabl total
        #current node processing before processing child

        #TC: O(n)
        #SC: O(height)



        self.total=0

        def dfs(node, n):
            if not node:
                return

            n = n*10+node.val

            if(not node.left and not node.right):
                self.total+=n
            
            dfs(node.left, n)
            dfs(node.right, n)
        
        if not root:
            return 0
        
        dfs(root, 0)

        return self.total