class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set('qwertyuiop')
        secondRow = set('asdfghjkl')
        thirdRow = set('zxcvbnm')
        ans = []
        for word in words:
            if(set(word.lower()).issubset(firstRow)):
                ans.append(word)
            elif(set(word.lower()).issubset(secondRow)):
                ans.append(word)
            elif(set(word.lower()).issubset(thirdRow)):
                ans.append(word)
        # print(ans)
        return ans