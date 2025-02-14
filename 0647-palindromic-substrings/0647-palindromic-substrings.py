class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0

        for center in range(len(s)):
            ans+=1
            left = center-1
            right = center+1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                ans+=1
                left-=1
                right+=1
            print(s[center])
            print(ans)
        
        for center in range(len(s)-1):
            center1 = center
            center2 = center+1
            if(s[center1]!=s[center2]):
                continue
            ans+=1
            left = center1-1
            right = center2+1
            while(left>=0 and right<len(s) and s[left]==s[right]):
                ans+=1
                left-=1
                right+=1
            print(ans)
        return ans