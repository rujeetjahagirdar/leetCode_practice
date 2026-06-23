class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word="balloon"

        freq = defaultdict(int)
        for i in text:
            freq[i]+=1
        
        #sinece 'balloon' have two l and two o, we divide their freq by 2,
        #so we would get potential number of 'balloon' strings we could form.

        freq['l']//=2
        freq['o']//=2

        print(freq)

        return(min(freq['o'], freq['b'], freq['a'], freq['l'], freq['n']))