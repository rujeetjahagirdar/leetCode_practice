class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            if(w not in curr.child):
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(curr, i):
            if(i==len(word)):
                return curr.is_end
            if(word[i]=='.'):
                # dfs
                for c in curr.child:
                    if dfs(curr.child[c], i+1):
                        return True
                return False
            else:
                if(word[i] not in curr.child):
                    return False
                curr = curr.child[word[i]]
                return dfs(curr, i+1)
        
        curr = self.root

        return dfs(curr, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)