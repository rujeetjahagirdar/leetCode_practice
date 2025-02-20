class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ['0']*len(nums[0])
        if(''.join(ans) not in nums):
            return ''.join(ans)

        i=0
        
        print(ans)
        while(i<len(ans)):
            j=len(ans)-1
            while(j>=i):
                ans[j]='1'
                print(ans)
                if(''.join(ans) not in nums):
                    print("Found")
                    return(''.join(ans))
                    # break
                if(j!=i):
                    ans[j]='0'
                    # print(ans)
                j-=1
            i+=1
        