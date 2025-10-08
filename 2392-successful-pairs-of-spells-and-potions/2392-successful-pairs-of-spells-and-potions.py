class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        potions.sort()

        def bSearch(nums, target):
            l=0
            r = len(nums)-1
            idx=-1

            while(l<=r):
                mid = l + (r-l)//2

                if(nums[mid]==target):
                    idx = mid
                    r = mid-1
                elif(target<nums[mid]):
                    idx = mid
                    r = mid-1
                else:
                    l=mid+1
            return idx
        
        for i in range(len(spells)):
            if(success%spells[i]==0):
                i = bSearch(potions, (success//spells[i]))
                if(i==-1):
                    ans.append(0)
                else:
                    ans.append(len(potions)-i)
            else:
                i = bSearch(potions, (success//spells[i] +1))
                if(i==-1):
                    ans.append(0)
                else:
                    ans.append(len(potions)-i)
        print(ans)
        return ans