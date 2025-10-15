# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        #dfs, bottom up
        #process current node after processing children

        self.ans=0

        def dfs(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtreeSum = (left_sum+right_sum+node.val)
            subtreeCount = (left_count+right_count+1)
            
            subtreeAvg = int(subtreeSum/subtreeCount)

            if(subtreeAvg==node.val):
                self.ans+=1
            
            return (subtreeSum, subtreeCount)
        
        dfs(root)

        return self.ans
