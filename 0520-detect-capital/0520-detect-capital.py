class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if(word.isupper()):
            return True
        if(word.islower()):
            return True
        
        if(ord('A')<=ord(word[0])<=ord('Z')):
            for i in range(1, len(word)):
                if(ord('A')<=ord(word[i])<=ord('Z')):
                    return False
            
            return True
        
        return False