class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = []
        words = sentence.split(" ")
        for i in range(len(words)):
            print(words[i])
            if(words[i][0] in 'aeiouAEIOU'):
                ans.append(words[i]+'ma'+'a'*(i+1))
            else:
                ans.append(words[i][1:]+words[i][0]+'ma'+'a'*(i+1))
        print(ans)
        return ' '.join(ans)