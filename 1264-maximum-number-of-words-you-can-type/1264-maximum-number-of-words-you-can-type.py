class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)

        words = text.split(" ")
        ans=0

        for word in words:
            for ch in word:
                if(ch in broken):
                    ans+=1
                    break
        
        return len(words)-ans