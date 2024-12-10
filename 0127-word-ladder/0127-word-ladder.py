class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        visited = set()


        def bfs(beginword):
            ans = float('inf')
            q = deque([(beginword, 1)])
            visited.add(beginword)

            while q:
                curr_word, curr_level = q.popleft()
                
                if(curr_word==endWord):
                    ans = min(ans, curr_level)
                
                for i in range(len(curr_word)):
                    for c in 'abcdefghijklmnopqrstuvxwyz':
                        new_word = curr_word[:i] + c +curr_word[i+1:]
                        if(new_word in wordList and new_word not in visited):
                            q.append((new_word, curr_level+1))
                            visited.add(new_word)
            if(ans==float('inf')):
                return 0
            else:
                return ans

        return(bfs(beginWord))