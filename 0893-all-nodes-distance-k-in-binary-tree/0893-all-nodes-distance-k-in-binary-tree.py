# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #dfs
        #making mapping for parent nodes {node: parent_node}
        #then from target node, go in direction of each of its child and parent and find nodes at k distance

        #TC: O(n)
        #SC: O(n)

        #make parent mapping
        parents = {}
        parents[root] = None

        def dfs(node):
            if(not node):
                return
            if(node.left):
                parents[node.left] = node
            if(node.right):
                parents[node.right] = node
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        #find nodes
        #dfs, top down

        ans=[]
        visited = set()

        def findNodes(nextNode, dist):
            if not nextNode or nextNode in visited:
                return
            visited.add(nextNode)
            if(dist==k):
                ans.append(nextNode.val)

            findNodes(nextNode.left, dist+1)
            findNodes(nextNode.right, dist+1)
            findNodes(parents[nextNode], dist+1)
        
        
        if(k==0):
            return [target.val]
            
        visited.add(target)
        for nxt in [target.left, target.right, parents[target]]:
            findNodes(nxt, 1)
        

        print(ans)
        return ans