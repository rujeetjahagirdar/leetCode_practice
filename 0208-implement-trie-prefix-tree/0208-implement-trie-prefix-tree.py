class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for w in word:
            charIndex = ord(w) - ord('a')
            # print(charIndex)
            if currentNode.child[charIndex]== None:
                currentNode.child[charIndex] = TrieNode()
            # print(currentNode.child)
            currentNode = currentNode.child[charIndex]
        currentNode.wordEnd = True
            
        

    def search(self, word: str) -> bool:
        currentNode = self.root
        for w in word:
            charIndex = ord(w) - ord('a')
            if(currentNode.child[charIndex])== None:
                return False
            currentNode = currentNode.child[charIndex]
        return currentNode.wordEnd

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for w in prefix:
            charIndex = ord(w) - ord('a')
            if(currentNode.child[charIndex])== None:
                return False
            currentNode = currentNode.child[charIndex]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)