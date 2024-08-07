class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def combineLists(ll1, ll2):
            ans=[]
            # print(ll1)
            for i in ll1:
                for j in ll2:
                    ans.append(i+j)
            # print(ans)
            return ans
        
        hashM = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'], 
                 '9':['w','x','y','z']}
        res=[]
        if not digits:
            return
        for i in digits:
            res.append(hashM[i])
        # print(res)
        while(len(res)>1):
            l1 = res.pop(0)
            # print(res)
            l2 = res.pop(0)
            res.insert(0,combineLists(l1, l2))
        return(res[0])