class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bsearch(arr, target):
            l=0
            r=len(arr)-1

            while(l<=r):
                mid = l+(r-l) //2

                if(arr[mid]==target):
                    return True
                elif(arr[mid]<target):
                    l=mid+1
                else:
                    r=mid-1
            return False        

        for i in range(len(matrix)):
            if(target>=matrix[i][0] and target<=matrix[i][-1]):
                return bsearch(matrix[i], target)
        
        return False