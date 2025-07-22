class Solution:
    def isValid(self, word: str) -> bool:
        words = set(word)

        if(len(word)>=3):
            vowelCondition = False
            ConsonantCondition = False
            
            for w in words:
                if(w not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'):
                    return False
                if(w in "AEIOUaeiou"):
                    vowelCondition = True
                if(w in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'):
                    ConsonantCondition = True
            if(vowelCondition and ConsonantCondition):
                return True
        
        return False