# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        # currSum = 0

        # def dfs(root, currSum):

        #     if not root:
        #         return False
            
        #     currSum +=root.val

        #     if(not root.left and not root.right):
        #         if(currSum==targetSum):
        #             return True
        #         else:
        #             return False
                
        #     return dfs(root.left, currSum) or dfs(root.right, currSum)
        
        # return dfs(root, 0)

        found=False
        def dfs(node, currSum):
            nonlocal found

            if not node:
                return
            
            currSum+=node.val

            if(not node.left and not node.right):
                if(currSum==targetSum):
                    print(currSum)
                    found=True
                    return 
            
            dfs(node.left, currSum)
            dfs(node.right, currSum)
        
        dfs(root, 0)
        return found