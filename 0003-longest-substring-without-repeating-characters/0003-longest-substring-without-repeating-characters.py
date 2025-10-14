class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans=0

        l=0

        for r in range(len(s)):
            if(s[r] not in window):
                window.add(s[r])

                ans = max(ans, len(window))
            
            else:
                while(s[r] in window):
                    window.remove(s[l])
                    l+=1

                window.add(s[r])

                ans = max(ans, len(window))
        return ans