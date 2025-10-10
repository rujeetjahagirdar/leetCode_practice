class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        # for s in strs:
        #     srtedS = ''.join(sorted(s))
        #     groups[srtedS].append(s)
        
        # return list(groups.values())

        for s in strs:
            counts = [0]*26

            for i in s:
                counts[ord(i)-ord('a')]+=1
            
            groups[tuple(counts)].append(s)
        
        return list(groups.values())