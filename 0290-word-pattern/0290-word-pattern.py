class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # # d = {}
        # # s = s.split(' ')
        # # for i in range(len(pattern)):
        # #     if(pattern[i] not in d):
        # #         d[pattern[i]] = s[i]
        # #     else:
        # #         if(s[i]!=d[pattern[i]]):
        # #             return False
        # # return True
        # patternMap ={}
        # sMap = {}
        # s = s.split(' ')
        # for i in range(len(pattern)):
        #     # print(pattern[i])
        #     # print(patternMap)
        #     # print(sMap)
        #     if(pattern[i] not in patternMap):
        #         patternMap[pattern[i]]=s[i]
        #     else:
        #         if patternMap[pattern[i]]!=s[i]:
        #             # print('in pattern')
        #             return False
        #     if(s[i] not in sMap):
        #         sMap[s[i]] = pattern[i]
        #     else:
        #         if sMap[s[i]]!=pattern[i]:
        #             # print("in map")
        #             return False
        # return True
        l = s.split(" ")

        if len(l)!=len(pattern):
            return False

        d ={}
        se=set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=l[i]:
                    return False
            else:
                if l[i] not in se:
                    d[pattern[i]]=l[i]
                    se.add(l[i])
                else:
                    return False
        
        return True

