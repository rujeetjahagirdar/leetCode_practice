class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        ans = []
        for x,y in points:
            distances.append((x**2)+(y**2))
        print(distances)
        maxDis = sorted(distances)[k-1]
        print(maxDis)
        for i in range(len(distances)):
            if(distances[i]<=maxDis):
                ans.append(points[i])
        print(ans)
        return ans