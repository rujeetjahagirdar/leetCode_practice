# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        #there should not be a valid tree node to right or down of the first null node

        if not root:
            return True

        q = deque([root])
        seenNull = False

        while q:
            n = q.popleft()

            if(n==None):
                seenNull = True
            else:
                if(seenNull==True):
                    return False
            
                q.append(n.left)
                q.append(n.right)

        return True