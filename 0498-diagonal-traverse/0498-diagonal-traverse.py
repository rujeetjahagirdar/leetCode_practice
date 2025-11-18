class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        diagonal_elements = defaultdict(list)

        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[i])):
                diagonal_elements[i+j].append(mat[i][j])
        
        # print(diagonal_elements)

        ans=[]

        for i in sorted(diagonal_elements.keys()):
            if(i%2==0):
                ans.extend(diagonal_elements[i])
            else:
                ans.extend(diagonal_elements[i][::-1])
        
        return(ans)