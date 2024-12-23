# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def checkOps(arr):
            ops = 0

            sortedArr = sorted(arr)
            value_index_origianl = {}
            
            for i in range(len(arr)):
                value_index_origianl[arr[i]]=i

            print(value_index_origianl)

            #swap the values in original array
            #update the value_index_origianl mapping after the updates
            #arr=[4,3,2,1]
            #sortedArr = [1,2,3,4]
            #value_index_origianl = {4:0, 3:1, 2:2, 1:3}
            for i in range(len(arr)):
                if(arr[i]!=sortedArr[i]):
                    ops+=1

                    n1_index = i
                    n2_index = value_index_origianl[sortedArr[i]]
                    
                    arr[n1_index], arr[n2_index] = arr[n2_index], arr[n1_index]

                    value_index_origianl[arr[n1_index]] = n1_index
                    value_index_origianl[arr[n2_index]] = n2_index

            print(ops)
            return ops
            
                
        # checkOps([20, 46, 15, 39])

        def bfs(node):
            if not root:
                return
            
            ans=0
            q = deque([root])

            while q:
                level_array = []

                for _ in range(len(q)):
                    n = q.popleft()
                    level_array.append(n.val)

                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)

                print(level_array)
                ans+=checkOps(level_array)
                print(ans)
            print(ans)
            return ans

        return(bfs(root))