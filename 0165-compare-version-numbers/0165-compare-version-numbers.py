class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #[1.0.1.02] [1.0.2]
        version1Array = version1.split(".")
        version2Array = version2.split(".")

        version1Array.extend([0]*max(0, len(version2Array)-len(version1Array)))
        version2Array.extend([0]*max(0, len(version1Array)-len(version2Array)))

        print(version1Array)
        print(version2Array)
        
        ans=0

        for i in reversed(range(len(version1Array))):
            if(int(version1Array[i])>int(version2Array[i])):
                ans=1
            elif(int(version1Array[i])==int(version2Array[i])):
               pass
            elif(int(version1Array[i])<int(version2Array[i])):
                ans=-1
        
        return(ans)

        
