class Solution:
    def sortSentence(self, s: str) -> str:
        ans=['']*len(s.split(' '))

        for i in s.split(" "):
            ans[int(i[-1])-1] = i[:-1]
        
        print(ans)
        return ' '.join(ans)