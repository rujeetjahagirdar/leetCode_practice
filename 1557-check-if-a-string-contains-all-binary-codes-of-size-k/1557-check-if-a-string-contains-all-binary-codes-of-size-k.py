class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        unique_sets = set()

        for i in range(0, len(s)-(k-1)):
            unique_sets.add(s[i:i+k])
        
        print(len(unique_sets))

        return len(unique_sets)==2**k