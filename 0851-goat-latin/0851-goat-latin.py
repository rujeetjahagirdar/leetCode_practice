class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans=[]
        words = sentence.split(' ')
        for i in range(len(words)):
            if(words[i][0].lower() in ('a','e','i','o','u')):
                ans.append(words[i]+'ma'+'a'*(i+1))
            elif(words[i][0].lower() not in ('a','e','i','o','u')):
                ans.append(words[i][1:]+words[i][0]+'ma'+'a'*(i+1))
            # else:
                # ans+=words[i]
        print(ans)
        return ' '.join(ans)
            