class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        d = {}
        ans = 0
        capacity = truckSize
        srt_boxes = sorted(boxTypes, key=lambda i:i[1], reverse=True)
        for bx in srt_boxes:
            if (bx[0]<capacity):
                ans +=bx[0]*bx[1]
                capacity -= bx[0]
            elif (bx[0]>=capacity):
                ans += (capacity) * bx[1]
                capacity -=capacity
        return(ans)
        
        