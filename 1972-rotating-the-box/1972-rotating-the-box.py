class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        for i in range(m):
            j, k = n-1, n-1
            while(j>=0):
                if(boxGrid[i][j]=='#'):
                    boxGrid[i][k], boxGrid[i][j] = boxGrid[i][j], boxGrid[i][k]
                    # print(boxGrid)
                    k-=1
                elif(boxGrid[i][j]=='*'):
                    k=j-1

                j-=1
        print(boxGrid)

        newBox = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                newBox[j][m-i-1] = boxGrid[i][j]
        print(newBox)
        return newBox