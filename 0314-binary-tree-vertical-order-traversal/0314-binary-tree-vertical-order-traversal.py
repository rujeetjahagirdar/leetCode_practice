# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if not root:
            return []
        
        column_node_mapping = defaultdict(list)

        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()

            column_node_mapping[col].append(node.val)

            if(node.left):
                q.append((node.left, col-1))
            if(node.right):
                q.append((node.right, col+1))
        
        # print(column_node_mapping)

        ans = []

        for i in sorted(column_node_mapping, key= lambda x: x):
            ans.append(column_node_mapping[i])
        
        print(ans)
        return ans