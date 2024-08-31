import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea = float("-inf")
        maxDia = float("-inf")
        for i in dimensions:
            dia = math.sqrt(i[0]*i[0] + i[1]*i[1])
            print(i, dia, i[0]*i[1])
            if(dia>maxDia):
                maxDia = dia
                maxArea = i[0]*i[1]
            elif(dia==maxDia):
                maxArea = max(maxArea, i[0]*i[1])
        print(maxArea)
        return maxArea
