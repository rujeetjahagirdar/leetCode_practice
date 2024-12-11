class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # [1, 2, 4, 6]


        def bSearch(arr, n):
            low=0
            high = len(arr)-1
            res = -1
            while(low<=high):
                mid = low + ((high-low)//2)
                # print(arr[mid])
                if(arr[mid]<=n):
                    res = mid
                    low = mid+1
                else:
                    high = mid-1
            # print(res)
            return res

        # print(bSearch([1,2, 4, 6], 5))
        # print(bSearch([1,1,1,1], 21))
        print(bSearch([9, 15, 75], 65))

        if(len(nums)==1):
            return 1

        ans = float("-inf")
        nums = sorted(nums)

        for i in range(len(nums)):
            upperBound = nums[i]+2*k
            j = bSearch(nums, upperBound)
            # print(nums[j])
            subSeqLength = (j-i)+1
            ans = max(ans, subSeqLength)
        print(ans)
        return ans

        #