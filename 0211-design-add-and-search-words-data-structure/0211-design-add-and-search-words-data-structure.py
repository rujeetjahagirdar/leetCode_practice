class TrieNode:
    def __init__(self):
        self.childNode = [None] * 26
        self.wordEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not currentNode.childNode[index]:
                currentNode.childNode[index] = TrieNode()
            currentNode = currentNode.childNode[index]
        currentNode.wordEnd = True

    def search(self, word: str) -> bool:
        def dfs(x, child):
            # print(child)
            currentNode = child
            # print(currentNode.childNode)
            for w in range(x, len(word)):
                # print(word[w])
                if(word[w]=='.'):
                    for i in currentNode.childNode:
                        if i:
                            if dfs(w+1, i):
                                return True
                    return False
                else:
                    index = ord(word[w]) - ord('a')
                    if currentNode.childNode[index]==None:
                        return False
                    currentNode = currentNode.childNode[index]
            # print(word, currentNode.wordEnd)
            return currentNode.wordEnd
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)