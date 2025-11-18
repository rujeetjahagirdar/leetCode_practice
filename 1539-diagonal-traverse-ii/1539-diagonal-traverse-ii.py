class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        diagonal_elements = defaultdict(list)

        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])):
                diagonal_elements[i+j].append(nums[i][j])
        
        print(diagonal_elements)
        
        ans=[]
        for i in sorted(diagonal_elements.keys()):
            ans.extend(diagonal_elements[i])
        
        return(ans)
        
        
        #################################
        # ans=[]

        # m = len(nums)

        # n=0
        # for i in nums:
        #     n = max(n, len(i))
        
        # for i in range(m):
        #     r=i
        #     c=0

        #     while(r>=0):
        #         if(c<len(nums[r])):
        #             ans.append(nums[r][c])
                
        #         r-=1
        #         c+=1
            
        #     # print(ans)
        
        # for i in range(1, n):
        #     r=m-1
        #     c=i
        #     # print(r, c)

        #     while(r>=0):
        #         if(c<len(nums[r])):
        #             ans.append(nums[r][c])
                
        #         r-=1
        #         c+=1
            
        #     # print(ans)
        
        
        # return ans