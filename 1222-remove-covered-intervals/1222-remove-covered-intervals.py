class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: (x[0], -x[1]))

        print(intervals)

        ans = []

        for interval in intervals:
            # print(interval)
            if(not ans or not (ans[-1][0]<=interval[0]<=ans[-1][1] and ans[-1][0]<=interval[1]<=ans[-1][1] and interval[0]<=interval[1])):
                ans.append(interval)
            
            print(ans)
        
        return len(ans)