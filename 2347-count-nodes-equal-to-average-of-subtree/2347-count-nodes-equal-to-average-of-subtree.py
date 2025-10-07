# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0

        def dfs_postOrder(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs_postOrder(node.left)
            right_sum, right_count = dfs_postOrder(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if(node.val==int(total_sum/total_count)):
                self.ans+=1
            
            return (total_sum, total_count)
        
        dfs_postOrder(root)

        return self.ans