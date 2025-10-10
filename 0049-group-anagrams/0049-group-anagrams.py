class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            srtedS = ''.join(sorted(s))
            groups[srtedS].append(s)
        
        return list(groups.values())