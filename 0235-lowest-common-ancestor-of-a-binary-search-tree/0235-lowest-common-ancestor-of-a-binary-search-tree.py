# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p_val = p.val
        # q_val = q.val

        # node = root

        # while node:
        #     parent_val = node.val

        #     if(p_val> parent_val and q_val>parent_val):
        #         node = node.right
            
        #     elif(p_val< parent_val and q_val<parent_val):
        #         node = node.left
            
        #     else:
        #         return node
        #################
        p_path = []
        q_path = []

        def dfs(node, target):

            if not node:
                return []

            stack = [(node, [node])]

            while stack:
                n, path = stack.pop()
                # print(n)
                if(n==target):
                    return path
                if(n.right):
                    stack.append((n.right, path+[n.right]))
                if(n.left):
                    stack.append((n.left, path+[n.left]))
            return []
        
        p_path = dfs(root, p)
        q_path = dfs(root, q)

        print(p_path)
        print(q_path)

        i=0
        ans=-1
        while(i<len(p_path) and i<len(q_path)):
            if(p_path[i] in q_path):
                ans = p_path[i]
            i+=1
        
        return(ans)