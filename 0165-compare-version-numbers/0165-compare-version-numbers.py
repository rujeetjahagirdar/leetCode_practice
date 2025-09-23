class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        if(len(v1)<len(v2)):
            v1.extend(['0']*(len(v2)-len(v1)))
        elif(len(v2)<len(v1)):
            v2.extend(['0']*(len(v1)-len(v2)))
        
        print(v1)
        print(v2)

        #1.2.2.2.3
        #1.2.2.3.2

        for i in range(len(v1)):
            if(int(v1[i])>int(v2[i])):
                return 1
            elif(int(v1[i])<int(v2[i])):
                return -1
        return 0