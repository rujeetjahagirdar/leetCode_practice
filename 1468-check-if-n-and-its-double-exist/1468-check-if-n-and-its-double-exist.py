class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        for i in range(len(arr)):
            if(arr[i]*2 in arr[i+1:] or arr[i]*2 in arr[:i]):
                return True
        return False