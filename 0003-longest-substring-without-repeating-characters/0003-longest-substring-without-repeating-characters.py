class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0

        l=0
        r=0

        sliding_window_set = set()

        while(r<len(s)):
            if(s[r] not in sliding_window_set):
                sliding_window_set.add(s[r])
                # print(sliding_window_set)
                ans = max(ans, len(sliding_window_set))
            else:
                while(s[l]!=s[r]):
                    sliding_window_set.remove(s[l])
                    l+=1
                sliding_window_set.remove(s[l])
                # print(sliding_window_set)
                l+=1
                sliding_window_set.add(s[r])
            r+=1
        print(ans)
        return ans