class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=0
        r = len(arr)-1

        while(l<=r):
            mid = (l+r)//2

            if(arr[mid]-mid-1 <k):
                l = mid+1
            else:
                r = mid - 1
        print(arr[r])
        return arr[r] + (k- (arr[r]-(r)-1))