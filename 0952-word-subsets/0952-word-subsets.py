class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def checkUniversal(c1, c2):
            #w1 = leetcode
            #w2 = loo
            # c1 = Counter(w1)
            # c2 = Counter(w2)

            for c in c2:
                if(c not in c1 or c1[c]<c2[c]):
                    return False
            return True

        # print(checkUniversal('leetcode', 'lo'))
        ans=[]

        newWord2C = Counter(words2[0])
        
        for i in range(1, len(words2)):
            for c in words2[i]:
                if(c in newWord2C):
                    newWord2C[c] = max(newWord2C[c], words2[i].count(c))
                else:
                    newWord2C[c] = words2[i].count(c)
        print(newWord2C)

        for word1 in words1:
            # flg=False
            c1 = Counter(word1)
            # for c2 in word2C:
            if(checkUniversal(c1, newWord2C)):
                ans.append(word1)
        
        print(ans)
        return ans