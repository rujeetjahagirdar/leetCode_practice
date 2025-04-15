class Trie:

    def __init__(self):
        self.trie = [None]*26 + [False]

    def insert(self, word: str) -> None:
        curr = self.trie

        for w in word:
            w_index = ord(w) - ord('a')
            if(curr[w_index]==None):
                curr[w_index] = [None]*26 + [False]
            
            curr = curr[w_index]

        curr[26] = True

    def search(self, word: str) -> bool:
        curr = self.trie

        for w in word:
            w_index = ord(w) - ord('a')
            if(curr[w_index]==None):
                return False
            curr = curr[w_index]
        if(curr[26]==True):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for w in prefix:
            w_index = ord(w) - ord('a')
            if(curr[w_index]==None):
                return False
            curr = curr[w_index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)