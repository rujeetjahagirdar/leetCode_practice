class Solution:
    def maxFreqSum(self, s: str) -> int:
        mxVowels = 0
        mxCons = 0

        c = Counter(s)

        for i in c:
            if(i in 'aeiou'):
                mxVowels = max(mxVowels, c[i])
            else:
                mxCons = max(mxCons, c[i])
        
        print(mxVowels)
        print(mxCons)
        return mxVowels+mxCons