class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        # ans=[]
        cnt=0
        # [3,6,1,2,5]
        # [1,2,3,5,6]

        i=0

        while(i<len(nums)):
            j=i+1
            # tAns=[nums[i]]
            while(j<len(nums) and (nums[j]-nums[i])<=k):
                j+=1
            # ans.append(nums[i:j])
            cnt+=1
            i=j
        # print(ans)
        print(cnt)
        return cnt
            