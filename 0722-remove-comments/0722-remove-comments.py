from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_block = False
        buffer = []

        for line in source:
            i = 0
            if not in_block:
                buffer = []

            while i < len(line):
                # Start of block comment
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True
                    i += 2

                # End of block comment
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False
                    i += 2

                # Line comment
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break

                # Normal character
                elif not in_block:
                    buffer.append(line[i])
                    i += 1

                else:
                    i += 1

            if not in_block and buffer:
                ans.append("".join(buffer))

        return ans