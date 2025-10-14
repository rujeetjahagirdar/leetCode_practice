class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        #-1 -> 25
        #find number of shits based on first char
        #and shift all other chars by this no of shits backword
            #if this results in number less than ord('a') then add 26

        #TC: O(no of strings * max of length of each string)
        #SC: O(no of strings * max of length of each string)

        hashM = defaultdict(list)

        for string in strings:
            if(string[0]=='a'):
                hashM[string].append(string)
            else:
                newStr = ''
                noOfShifts = ord(string[0]) - ord('a') #no of shifts based on first char
                for c in string:
                    newC = ord(c) - noOfShifts
                    if(newC<ord('a')):
                        newC = newC + 26
                    newStr+= chr(newC)
                
                hashM[newStr].append(string)
        
        return list(hashM.values())
