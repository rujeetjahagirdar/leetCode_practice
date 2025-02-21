# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.treeLevels = []
        self.q = deque([root])
        self.elements = set()
        root.val = 0
        while(self.q):
            t = []
            for i in range(len(self.q)):
                n = self.q.popleft()

                t.append(n.val)
                self.elements.add(n.val)
                if(n.left and n.left.val==-1):
                    # print("Left")
                    v = (2*n.val)+1
                    n.left.val = v
                    # print("v",v)
                    self.q.append(n.left)
                
                if(n.right and n.right.val==-1):
                    v = (2*n.val)+2
                    n.right.val = v
                    self.q.append(n.right)
                # if(not n.left and not n.right):
                #     continue
                # if(not n.left and n.right):
                #     self.q.append(TreeNode(-2))
                # if(not n.right and n.left):
                #     self.q.append(TreeNode(-2))
                # # print("t= ", t)
            self.treeLevels.append(t)
            print(self.treeLevels)
            print(self.elements)


    def find(self, target: int) -> bool:
        if target in self.elements:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)