class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        #[1,1,1,1]
        #[0,1,0,1]
        #[1,1,1,0]
        #[0,1,0,1]

        original=[-1]*len(derived)

        for i in range(len(derived)):
            if(i==len(derived)-1):
                if(derived[i]==0):
                    if(original[i]==original[0]):
                        return True
                    else:
                        return False
                else:
                    if(original[i]!=original[0]):
                        return True
                    else:
                        return False
            elif(i==0):
                if(derived[i]==0):
                    original[i]=0
                    original[i+1]=0
                else:
                    original[i]=0
                    original[i+1]=1
            else:
                if(derived[i]==0):
                    # original[i]=0
                    original[i+1]=original[i]
                else:
                    # original[i]=0
                    original[i+1]=int(not original[i])
            # print(original)