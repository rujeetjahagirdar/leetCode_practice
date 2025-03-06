class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        c = Counter(arr)
        sorted_c = sorted(c, key=lambda x:c[x], reverse=True)
        ans=0
        total=0

        print(sorted_c)
        for i in sorted_c:
            total+=c[i]
            ans+=1
            if(total>=n//2):
                break
        
        print(ans)
        return ans