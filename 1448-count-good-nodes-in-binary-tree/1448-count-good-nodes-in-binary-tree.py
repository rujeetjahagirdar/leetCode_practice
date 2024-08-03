# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count =0
        mx = root.val
        def dfs(node, mx):
            nonlocal count
            if not node:
                return 0
            print("Node= ",node.val)
            if node.val>=mx:
                count = count + 1
                print(count)
                mx=node.val
            dfs(node.left, mx)
            dfs(node.right, mx)
            return
        dfs(root, root.val)
        print(count)
        return count