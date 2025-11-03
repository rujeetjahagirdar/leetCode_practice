class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        ans = (float("inf"), None, None) #minlen, start index, end index

        target_freq = Counter(t)

        l=0
        matched_chars = 0
        window_freq = Counter()

        for r in range(len(s)):
            window_freq[s[r]]+=1

            if(window_freq[s[r]]==target_freq[s[r]]):
                matched_chars+=1
            
            while(l<=r and matched_chars==len(target_freq)):
                #its a valid window, update ans
                current_window_size = (r-l)+1
                if(current_window_size<ans[0]):
                    ans = (current_window_size, l, r)
                
                #reduce window from left
                # window_freq[s[l]]-=1
                if(window_freq[s[l]]==target_freq[s[l]]):
                    matched_chars-=1
                window_freq[s[l]]-=1

                l+=1
        print(ans)
        if(ans[0]==float("inf")):
            return ""
        else:
            return s[ans[1]:ans[2]+1]
            