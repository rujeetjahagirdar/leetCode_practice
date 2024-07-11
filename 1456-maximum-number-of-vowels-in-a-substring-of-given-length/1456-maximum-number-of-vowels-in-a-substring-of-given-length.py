class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # ans=0
        vowels = ('a','e','i','o','u')
        # def countVowels(s):
        #     vowels = ('a','e','i','o','u')
        #     return sum(1 for c in s if c in vowels)
        # for i in range(len(s)-(k-1)):
        #     vowelCOunt=0
        #     substr = s[i:i+k]
        #     # for j in substr:
        #     #     if j in ('a','e','i','o','u'):
        #     #         vowelCOunt = vowelCOunt +1
        #     vowelCOunt = countVowels(substr)
        #     if vowelCOunt>ans:
        #         ans= vowelCOunt
        # print(ans)
        # return ans
        ans=0
        currentCount= sum(1 for c in s[:k] if c in vowels)
        ans=currentCount
        # print(s[:k], currentCount)
        for i in range(1,len(s)-(k-1)):
            if(s[i-1] in vowels):
                currentCount = currentCount -1
            if(s[i+k-1] in vowels):
                currentCount = currentCount +1
            if(currentCount>ans):
                ans=currentCount
            # print(s[i:i+k], currentCount)
        print(ans)
        return ans