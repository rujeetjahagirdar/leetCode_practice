class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans= []
        words = sentence.split(" ")
        for i in range(len(words)):
            if(words[i][0] in 'aeiouAEIOU'):
                t = words[i][:]+"ma"+"a"*(i+1)
            else:
                t = words[i][1:]+words[i][0]+"ma"+'a'*(i+1)
            ans.append(t)
        return " ".join(ans)