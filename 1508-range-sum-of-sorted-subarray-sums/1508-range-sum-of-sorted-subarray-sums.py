class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subArraySum=[]
        for i in range(len(nums)):
            t=[nums[i]]
            for j in range(i+1, len(nums)):
                t.append(t[-1]+nums[j])
            # print(t)
            # break
            subArraySum.extend(t)
        # print(subArraySum)
        return(sum(sorted(subArraySum)[left-1:right]) % (10**9 +7))