class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_to_word = defaultdict(set)

        for word in dictionary:
            self.abbr_to_word[self.abbr(word)].add(word)
        
        print(self.abbr_to_word)

        

    def isUnique(self, word: str) -> bool:
        abr = self.abbr(word)
        if(abr not in self.abbr_to_word):
            return True
        
        if(len(self.abbr_to_word[abr])==1 and self.abbr_to_word[abr]=={word}):
            return True
        
        return False
    
    def abbr(self, word: str) -> str:
        if(len(word)<2):
            return word
        abbr = word[0]+str(len(word[1:-1]))+word[-1]
        print(word, abbr)
        
        return abbr


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)