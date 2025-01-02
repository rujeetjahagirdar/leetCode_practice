class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # valid_indexs = []
        # vowels = set(['a','e','i','o','u'])

        # for i in range(len(words)):
        #     if(words[i][0] in vowels and words[i][-1] in vowels):
        #         valid_indexs.append(i)
        
        # print(valid_indexs)

        # ans=[]

        # for start, end in queries:
        #     count=0
        #     for i in valid_indexs:
        #         if(start<=i<=end):
        #             count+=1
        #     ans.append(count)
        
        # print(ans)
        # return ans
        ##############################
        vowels = set(['a','e','i','o','u'])
        prefixUptoCount = [0]*len(words)

        def isValidWord(w):
            if(w[0] in vowels and w[-1] in vowels):
                return True
            return False

        for i in range(0, len(words)):
            if(isValidWord(words[i])):
                prefixUptoCount[i] = prefixUptoCount[i-1]+1
            else:
                prefixUptoCount[i] = prefixUptoCount[i-1]
        
        print(prefixUptoCount)

        ans=[]

        for start, end in queries:
            if(start==0):
                ans.append(prefixUptoCount[end])
            else:
                ans.append(prefixUptoCount[end]-prefixUptoCount[start]+isValidWord(words[start]))
        print(ans)
        return ans