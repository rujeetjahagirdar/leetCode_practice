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

        if not root:
            return 0

        self.ans=0

        def traverse(node, n):
            if not node:
                return
            
            current_num = n*10 + node.val
            
            if(not node.left and not node.right):
                self.ans+=current_num
            
            traverse(node.left, current_num)
            traverse(node.right, current_num)
        

        traverse(root, 0)

        return self.ans