class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #arr = [1,0,2,3,4]
        ans=0

        i=0
        j=0
        while(j<len(arr) and i<len(arr)):
            # print(arr[i:j])
            while(j!=max(arr[:j+1])):
                j+=1
            ans+=1
            i=j+1
            j=i
        print(ans)
        return ans