# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.flattened_array = []
        self.pointer=-1
        self._inorderTraverse(root)

    def _inorderTraverse(self, root):
        if not root:
            return
        self._inorderTraverse(root.left)
        self.flattened_array.append(root.val)
        self._inorderTraverse(root.right)

    def next(self) -> int:
        self.pointer+=1
        return self.flattened_array[self.pointer]

    def hasNext(self) -> bool:
        if(self.pointer+1<len(self.flattened_array)):
            return True
        else:
            return False        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()