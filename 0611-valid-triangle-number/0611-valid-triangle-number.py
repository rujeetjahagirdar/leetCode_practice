class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # def  bsearch(a, t):
        #     l=0
        #     r = len(a)-1
        #     ans = len(a)

        #     while(l<=r):
        #         mid = (l+r)//2

        #         if(a[mid]>=t):
        #             ans=mid
        #             r=mid-1
        #         else:
        #             l=mid+1
            
        #     return ans
     

        # ans=0
        # nums.sort()
        # #[2,2,3,4]
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         k = j+1+bsearch(nums[j+1:], nums[i]+nums[j])
        #         # if(k!=-1):
        #         # print(k)
        #         # print(nums[i], nums[j], nums[k-1])
        #         if((nums[i]+nums[j])<=nums[k-1]):
        #             continue
        #         ans+=(k-1 - j)
        #         # print(ans)
        # return ans
        


        ans=0
        nums.sort()
        #[2,2,3,4]

        for k in range(len(nums)-1, 1, -1):
            c = nums[k]

            l=0
            r = k-1

            while(l<r):
                if(nums[l]+nums[r]<=c):
                    l+=1
                else:
                    ans+=(r-l)
                    r-=1
            # print(ans)
        return ans