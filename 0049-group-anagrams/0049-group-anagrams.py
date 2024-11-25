class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==0 or len(strs)==1):
            return [strs]
        else:
            hashM = defaultdict(list)
            for s in strs:
                sorted_s = ''.join(sorted(s))
                # print(sorted_s)
                # if(sorted_s not in hashM):
                hashM[sorted_s].append(s)
        print(list(hashM.values()))
        return list(hashM.values())