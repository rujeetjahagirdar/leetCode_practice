class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        #calculate sum of all abs values of elements
        #also keep count of negative values
        #keep the min abs value in matrix
        #if count of negative values is odd 
            #subtract 2 times min abs value from total sum
                #because if its odd, then in the end we will have exactly one negative number          #and we want this negative number to have smallest abs value so that it will maximize the overall sum of matrix
                #with multiple oprations we can transfer this last negative number to smallest abs value element, so we will subtract this smallest abs value two times since we had summed it already
                # and if count of negative numbers is even, then in the end we will have 0 negative numbers after performing mutiple operations

        ans = 0
        count_of_negatives = 0
        min_absolute_number = float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans+=abs(matrix[i][j])
                if(matrix[i][j]<0):
                    count_of_negatives+=1
                min_absolute_number = min(min_absolute_number, abs(matrix[i][j]))
        
        if(count_of_negatives%2==0):
            return ans
        else:
            ans-= (2* min_absolute_number)
            return ans