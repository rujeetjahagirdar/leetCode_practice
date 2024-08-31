class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if(str1 == str2[:len(str1)] and str1==str2[-len(str1):]):
                return True
            return False
        ans=0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if(len(words[i])<=len(words[j])):
                    if(isPrefixAndSuffix(words[i], words[j])):
                        ans +=1
        print(ans)
        return ans