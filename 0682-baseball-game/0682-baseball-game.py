class Solution:
    def calPoints(self, operations: List[str]) -> int:
        socres = []
        for i in operations:
            if i=='+':
                socres.append(int(socres[-1])+int(socres[-2]))
            elif i=='C':
                socres.pop()
            elif i=='D':
                socres.append(int(socres[-1])*2)
            else:
                socres.append(int(i))
            print(socres)
        return sum([int(i) for i in socres])