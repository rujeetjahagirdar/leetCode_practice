class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)

        for i in range(len(wordsDict)):
            self.words[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ans=float('inf')
        # print(self.words)
        for i1 in self.words[word1]:
            for i2 in self.words[word2]:
                ans = min(ans, abs(i2-i1))
        
        return(ans)


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)