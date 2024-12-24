from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Count the frequency of each character in chars
        chars_count = Counter(chars)
        
        total_length = 0
        
        # Iterate through each word in the words list
        for word in words:
            word_count = Counter(word)  # Count the frequency of each character in the word
            
            # Check if the word can be formed
            can_form = True
            for char, count in word_count.items():
                if chars_count[char] < count:  # If chars does not have enough of this character
                    can_form = False
                    break
            
            if can_form:  # If the word can be formed, add its length to total_length
                total_length += len(word)
        
        return total_length
