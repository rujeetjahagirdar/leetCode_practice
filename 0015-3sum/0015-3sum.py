class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        nums.sort()
#        [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):

            if(i>0 and nums[i]==nums[i-1]):
                continue

            l = i+1
            r = len(nums)-1

            while(l<r):
                s = nums[l]+nums[r]
                if(s==-nums[i]):
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                    while(r>l and nums[r+1]==nums[r]):
                        r-=1

                elif(s<-nums[i]):
                    l+=1
                else:
                    r-=1
        print(ans)
        return ans