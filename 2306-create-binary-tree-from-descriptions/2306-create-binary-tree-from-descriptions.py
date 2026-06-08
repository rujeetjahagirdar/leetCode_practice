# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childrens = set()
        for parent, child, isLeft in descriptions:
            if(parent not in nodes):
                pNode = TreeNode(parent)
            else:
                pNode = nodes[parent]
            if(child not in nodes):
                cNode = TreeNode(child)
            else:
                cNode = nodes[child]
            
            if(isLeft):
                pNode.left = cNode
            else:
                pNode.right = cNode
            
            nodes[parent] = pNode
            nodes[child] = cNode

            childrens.add(child)
            
        
        # print(nodes)

        for val in nodes:
            if(val not in childrens):
                return nodes[val]

