class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0, len(arr)-2):
            print(arr[i])
            if((arr[i]*arr[i+1]*arr[i+2])%2!=0):
                return True
        return False