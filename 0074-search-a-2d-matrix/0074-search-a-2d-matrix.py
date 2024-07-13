class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch2(arr, low, high, target):
            # print(arr,low, high)
            if(high>=low):
                mid = (high+low)//2
                if(arr[mid]==target):
                    return True
                elif(target<arr[mid]):
                    return binarySearch2(arr, low, mid-1, target)
                else:
                    return binarySearch2(arr, mid+1, high, target)
            return False
        
        def binarySearch(matrix,low, high, target):
            if(high>=low):
                mid = (high+low)//2
                # print(matrix[mid][0])
                if(matrix[mid][0]<=target and matrix[mid][-1]>=target):
                    return(binarySearch2(matrix[mid],0, len(matrix[mid])-1,target))
                elif(target<matrix[mid][0]):
                    return binarySearch(matrix, low, mid-1, target)
                elif(target>matrix[mid][-1]):
                    return binarySearch(matrix, mid+1, high, target)
            return False
        return(binarySearch(matrix, 0, len(matrix)-1, target))
        # return(binarySearch(matrix, 0, len(matrix), target))