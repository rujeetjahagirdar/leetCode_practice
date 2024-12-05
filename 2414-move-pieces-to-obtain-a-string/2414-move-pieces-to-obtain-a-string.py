class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #both letters can not cross each other
        #'L' can go only left i.e. 'L' in start should be equal or right of the corresponding 'L' in target
        #'R' can go only left i.e. 'R' in start should be equal or left of the corresponding 'R' in target
        startArray = []
        targetArray = []

        for i in range(len(start)):
            if(start[i] in ('R', 'L')):
                startArray.append((start[i], i))
            if(target[i] in ('R', 'L')):
                targetArray.append((target[i], i))
        
        print(startArray)
        print(targetArray)

        if(len(startArray)!=len(targetArray)):
            return False
        
        for i in range(len(startArray)):
            if(startArray[i][0]!=targetArray[i][0]):
                return False
            if(startArray[i][0]=='L'):
                if(startArray[i][1]<targetArray[i][1]):
                    return False
            elif(startArray[i][0]=='R'):
                if(startArray[i][1]>targetArray[i][1]):
                    return False
        return True