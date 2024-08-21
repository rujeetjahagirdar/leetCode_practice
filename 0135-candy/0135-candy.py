class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                ans[i] =ans[i-1]+1
        # print(ans)
        ratings = ratings[::-1]
        ans = ans[::-1]
        print(ratings)
        print(ans)
        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                if(ans[i-1]+1>ans[i]):
                    ans[i] = ans[i-1]+1
        print(ans)
        return(sum(ans))