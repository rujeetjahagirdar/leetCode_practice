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

        node_parent_mapping = {}
        def traverse(node, parent_node):
            if not node:
                return
            
            node_parent_mapping[node] = parent_node

            traverse(node.left, node)
            traverse(node.right, node)

        traverse(root, None)

        ans=[]
        visited = set()

        def findNodes(node, nextNode, dist):
            if(not nextNode or nextNode in visited):
                return
            visited.add(nextNode)
            if(dist==0):
                ans.append(nextNode.val)
            
            findNodes(nextNode, nextNode.left, dist-1)
            findNodes(nextNode, nextNode.right, dist-1)
            findNodes(nextNode, node_parent_mapping[nextNode], dist-1)

            return
        
        if(k==0):
            return [target.val]

        visited.add(target)
        for nextNode in [target.left, target.right, node_parent_mapping[target]]:
            # visited.add(nextNode)
            findNodes(target, nextNode, k-1)
        
        return ans
