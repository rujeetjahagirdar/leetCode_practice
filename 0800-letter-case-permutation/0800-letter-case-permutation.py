class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans=[]

        t = []

        #t=[a1, A1]
        #ans = [a1b, a1B, A1b, A1B]
        #

        for i in s:
            if(i.isalpha()):
                if(not t):
                    t.append(i.lower())
                    t.append(i.upper())
                else:
                    n = len(t)
                    for j in range(len(t)):
                        t.append(t[j]+i.lower())
                        t.append(t[j]+i.upper())

                        # del t[i]
                    t = t[n:]
            else:
                if(not t):
                    t.append(i)
                else:
                    n = len(t)
                    for j in range(len(t)):
                        t.append(t[j]+str(i))
                    t = t[n:]
            print(t)
        return t
        