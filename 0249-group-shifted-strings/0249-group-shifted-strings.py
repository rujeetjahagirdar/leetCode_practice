class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        groups = {}

        for i in range(len((strings))):
            shiftedStr = ''

            if(strings[i][0]!='a'):
                #shift the string
                noOfShits = ord(strings[i][0]) - ord('a')

                # shiftedStr = ''
                for c in strings[i]:
                    zeroBasedIndex = ord(c)-ord('a')
                    shiftedIndex = zeroBasedIndex - noOfShits
                    roundedIndex = (shiftedIndex)%26 + ord('a')
                    shiftedStr+=chr(roundedIndex)
                print(strings[i], shiftedStr)
            else:
                shiftedStr = strings[i]
            
            if(shiftedStr in groups):
                groups[shiftedStr].append(strings[i])
            else:
                groups[shiftedStr] = [strings[i]]
            # print(groups)
            
        ans=[]

        for i in groups:
            ans.append(groups[i])
        return ans