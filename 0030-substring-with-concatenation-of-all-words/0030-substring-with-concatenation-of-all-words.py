class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordCount = Counter(words)
        ans=[]
        total_length = len(words[0]) * len(words)
        n = len(words[0])
        for i in range(0, len(s)-total_length+1):
            t = s[i:i+total_length]
            # print(i, t)
            t_list = [t[j:j+n] for j in range(0,len(t), n)]
            # print(t_list)
            tCount = Counter(t_list)
            if(wordCount==tCount):
                ans.append(i)
                # print(ans)
        return ans