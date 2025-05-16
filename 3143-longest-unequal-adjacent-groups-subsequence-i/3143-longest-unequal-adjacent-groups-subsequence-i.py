class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # longest = 0
        # seq_idx = []
        # ans=[]

        # i=0
        # # seq_idx.append(i)
        # while(i<len(groups)):
        #     seq_idx.append(i)
        #     print(seq_idx)
        #     j=i+1
        #     if(j>=len(groups)):
        #         if(len(seq_idx)>len(ans)):
        #             ans = [words[i] for i in seq_idx]
        #             seq_idx = []
        #         break
            
        #     while(j<len(groups) and groups[j]!=groups[j-1]):
        #         seq_idx.append(j)
        #         print(seq_idx)
        #         j+=1
            
        #     if(len(seq_idx)>len(ans)):
        #         ans = [words[i] for i in seq_idx]
        #         seq_idx = []
        #         print("ans= ", ans)
        #     i=j
        #     seq_idx = []
        
        # return(ans)
        #############
        stack = [0]

        for i in range(1, len(groups)):
            if(groups[i]!=groups[stack[-1]]):
                stack.append(i)
        
        print(stack)

        return ([words[i] for i in stack])