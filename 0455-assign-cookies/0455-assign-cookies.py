class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans =0 
        i = j=0
        g.sort()
        s.sort()
        print(g)
        print(s)
        while(i<len(g) and j<len(s)):
            if(s[j]>=g[i]):
                ans +=1
                i +=1
            j +=1
            # else:
            #     break
        print(ans)
        return ans