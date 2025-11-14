class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #stack
        intervals = sorted(intervals, key=lambda x: x[0])


        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if(s<=stack[-1][1]): #overlap
                stack[-1][1] = max(e, stack[-1][1])
            else:
                stack.append([s, e])
        
        return stack