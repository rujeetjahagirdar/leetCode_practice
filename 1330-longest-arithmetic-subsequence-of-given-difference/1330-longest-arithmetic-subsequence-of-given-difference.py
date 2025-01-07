class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        #arr = [1,5,7,8,5,3,4,2,1], difference = -2
        dp ={}
        ans= float("-inf") 

        for i in range(len(arr)):
            if(arr[i]-difference in dp):
                dp[arr[i]] = dp[arr[i]-difference]+1
            else:
                dp[arr[i]]=1
            ans=max(ans, dp[arr[i]])
            
        print(dp)
        return(ans)