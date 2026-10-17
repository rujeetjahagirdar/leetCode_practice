class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        temp = []

        for i in range(len(nums)):
            dSum=0
            for c in str(nums[i]):
                dSum+=int(c)
            
            temp.append((dSum, nums[i], i))
        
        # print(temp)
        temp = sorted(temp, key = lambda x: (x[0], x[1]))

        # print(temp)

        ans=0
        seen = set()

        for i in range(len(temp)):
            if(i not in seen):
                j= i
                seen.add(j)
                while(temp[j][2]!=i):
                    j = temp[j][2]
                    ans+=1
                    seen.add(j)
        
        return(ans)