# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        array = []

        def inorder(node):
            if not node:
                return 
            # if not node.left and not node.right:
            #     array.append(node.val)
            
            if node.left:
                inorder(node.left)
            array.append(node.val)
            if node.right:
                inorder(node.right)
        

        inorder(root)
        print(array)
        ans=float("inf")

        for i in range(len(array)-1):
            ans = min(ans, abs(array[i]- array[i+1]))
        print(ans)
        return ans