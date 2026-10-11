class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)[2:]

        compNum = ''.join(['1' if i=='0' else '0' for i in binNum])

        return int(compNum, 2)
