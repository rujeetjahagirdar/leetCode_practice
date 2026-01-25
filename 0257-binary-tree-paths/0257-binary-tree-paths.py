# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        # def dfs(node, path):
        #     if not node:
        #         return
        #     if not node.left and not node.right:
        #         path.append(str(node.val))
        #         # print(path)
        #         ans.append('->'.join(path))
        #         # print("ans", ans)
        #         path.pop()
        #         return
            
        #     path.append(str(node.val))
        #     # print(path)
        #     dfs(node.left, path)
        #     dfs(node.right, path)
        #     path.pop()
        #     return

        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))

            if(not node.left and not node.right):
                ans.append("->".join(path))
            
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
            return 
    
        dfs(root, [])
        return(ans)