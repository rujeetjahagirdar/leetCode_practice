class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=max(piles)
        # if(len(piles)==1):
        #     return (piles[0]//h)+1
        # elif(len(piles)==h):
        #     return max(piles)
        # else:
            # for i in range(1,max(piles)+1):
            #     # print("i= ",i)
            #     count =0
            #     for b in piles:
            #         count+=(b//i)+1 if b%i!=0 else (b//i)
            #         # print("count= ",count)
            #         if(count>h):
            #             break
            #     if(count<=h):
            #         ans = i
            #         break
            # # print(ans)
            # return ans
        low = 1
        high = max(piles)
        while(low<=high):
            count = 0
            mid = low+(high-low)//2
            print(low,high,mid)
            for b in piles:
                count+=(b//mid)+1 if b%mid!=0 else (b//mid)
                # print("count= ",count)
                if(count>h):
                    # low = mid+1
                    # print("Updated l= ",low)
                    break
            print("Count =", count)
            if(count>h):
                print("Count is greater than h")
                # ans = mid
                low = mid+1
            elif(count<=h):
                ans = min(mid, ans)
                high = mid -1
                print("Updated h= ",high, count)
        print(ans)
        return ans
