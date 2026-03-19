class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        occurances = defaultdict(list)

        for i in range(len(s)):
            if(s[i] in occurances):
                occurances[s[i]][-1] = i
            else:
                occurances[s[i]].extend([i, i])
        
        # print(occurances)

        i=0
        while(i<len(s)):
            j=i
            end = occurances[s[j]][-1]

            while(j<len(s) and j<end):
                end = max(end, occurances[s[j]][-1])
                j+=1
            ans.append(j-i +1)

            i=j+1

        print(ans)
        return ans