class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # ans=[]
        # i=0
        # j=0

        # while(i<len(s) and j<len(spaces)):
        #     if(i<spaces[j]):
        #         ans.append(s[i])
        #         i+=1
        #     else:
        #         ans.append(" ")
        #         j+=1
        
        # if(i<len(s)):
        #     while(i<len(s)):
        #         ans.append(s[i])
        #         i+=1
        # print(ans)
        # return ''.join(ans)

        ans=''

        i=0
        for j in spaces:
            ans+=s[i:j]
            ans+=" "
            i=j

        if(i<len(s)):
            ans+=s[i:]
        print(ans)
        return ans

