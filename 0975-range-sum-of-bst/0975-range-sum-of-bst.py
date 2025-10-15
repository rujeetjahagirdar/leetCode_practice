# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        #dfs, top down
        #store in global list

        ans = []

        def traverse(node, low, high):
            if not node:
                return
            
            if(low<=node.val<=high):
                ans.append(node.val)
                traverse(node.left, low, node.val)
                traverse(node.right, node.val, high)
            elif(node.val<low):
                traverse(node.right, low, high)
            elif(node.val>high):
                traverse(node.left, low, high)


        traverse(root, low, high)

        return sum(ans)