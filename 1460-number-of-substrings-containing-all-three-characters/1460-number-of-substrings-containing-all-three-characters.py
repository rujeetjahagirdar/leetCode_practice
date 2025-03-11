class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # ans=0

        # l=0
        # counts = defaultdict(int)
        
        # for r in range(len(s)):
        #     counts[s[r]]+=1
        #     # print(counts)
        #     if(len(counts)==3):
        #         # ans+=1
        #         # ans+=(len(s)-(r))
        #         # print(ans)

        #         while(len(counts)==3):
        #             # print(s[l])
        #             ans+=(len(s)-(r))
        #             counts[s[l]]-=1
        #             if(counts[s[l]]==0):
        #                 counts.pop(s[l])
        #             # print(counts)
        #             # ans+=1
        #             l+=1
        #     print(ans)
        # return ans
        ####################
        ans=0

        latest_idx = {'a':-1, 'b':-1, 'c':-1}
        
        for i in range(len(s)):
            latest_idx[s[i]]=i

            if(latest_idx['a']!=-1 and latest_idx['b']!=-1 and latest_idx['c']!=-1):
                ans+=(1+ min(latest_idx['a'], latest_idx['b'], latest_idx['c']))
        return ans