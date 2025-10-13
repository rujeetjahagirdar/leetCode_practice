class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #first sort input based on first value (start time)
        #then use stack and append intervals my merging with stack -1

        #TC : O(n logn)
        #SP : O(n)

        sorted_intervals = sorted(intervals, key= lambda x: x[0])

        stack = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            s, e = sorted_intervals[i]

            if(stack[-1][0]<=s<=stack[-1][1]):
                stack[-1][1] = max(stack[-1][1], e)
            
            else:
                stack.append([s, e])
        
        return stack