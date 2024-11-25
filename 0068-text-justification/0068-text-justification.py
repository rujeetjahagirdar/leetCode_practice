class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[]
        line = []
        length_line = 0

        for word in words:

            if(length_line + len(line) + len(word))<=maxWidth:  # len(line) will be number of single space after each word, and length_line will be length of line without cosidering one space after each word.
                line.append(word)
                length_line +=len(word)
            else:
                empty_spaces_to_fill = (maxWidth - length_line)
                slots_for_empty_spaces = len(line)-1 or 1  #if there are 3 words in line then there are 2 slots each after every word except last word and if there is only one word then only one slot after this one word
                for i in range(empty_spaces_to_fill):
                    line[i% slots_for_empty_spaces] +=' '  #append one space to each slot one by one in circular manner
                result.append(''.join(line))
                line = [word]
                length_line=len(word)
                print(result)
        
        last_line = ' '.join(line).ljust(maxWidth)
        result.append(last_line)

        print(result)
        return result