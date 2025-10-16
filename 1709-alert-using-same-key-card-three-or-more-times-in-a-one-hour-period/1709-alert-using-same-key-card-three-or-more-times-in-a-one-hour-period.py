class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hashM = defaultdict(list)

        for i in range(len(keyName)):
            h,m = keyTime[i].split(":")
            time = int(h)*60 + int(m)

            hashM[keyName[i]].append(time)
        
        ans=[]

        for i in hashM:
            if(len(hashM[i])>=3):
                hashM[i].sort()
                for j in range(len(hashM[i]) -2):
                    if((hashM[i][j+2] - hashM[i][j])<=60):
                        ans.append(i)
                        break
        
        ans.sort()
        return ans

