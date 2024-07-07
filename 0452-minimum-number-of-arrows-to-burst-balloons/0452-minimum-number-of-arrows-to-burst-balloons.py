class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def isOverlap(i1,i2):
            # print(i1,i2)
            if(i2[0]>=i1[0] and i2[0]<=i1[1]):
                return True
            return False
        count=1
        points.sort()
        prevOverlap = points[0]
        # print(points)
        for i in points[1:]:
            # print(i)
            if isOverlap(prevOverlap, i):
                prevOverlap = [max(prevOverlap[0],i[0]), min(prevOverlap[1],i[1])]
            else:
                count = count + 1
                prevOverlap = i
            # print(count)
        print(count)
        return count