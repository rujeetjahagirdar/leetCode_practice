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

        # found=False
        # def dfs(node, currSum):
        #     nonlocal found

        #     if not node:
        #         return
            
        #     currSum+=node.val

        #     if(not node.left and not node.right):
        #         if(currSum==targetSum):
        #             print(currSum)
        #             found=True
        #             return 
            
        #     dfs(node.left, currSum)
        #     dfs(node.right, currSum)
        
        # dfs(root, 0)
        # return found

        ##### Early termination

        def dfs(node, currSum):
            if not node:
                return False
            
            currSum+=node.val

            if(not node.left and not node.right):
                if(currSum==targetSum):
                    return True
            
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        
        return dfs(root, 0)
        