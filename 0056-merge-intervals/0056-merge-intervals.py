class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sorting + stack
        stack = []

        intervals2 = sorted(intervals, key = lambda x: x[0])

        stack.append(intervals2[0])

        for i in range(1, len(intervals2)):
            if(intervals2[i][0]<=stack[-1][1]):
                stack[-1][1] = max(intervals2[i][1], stack[-1][1])
            else:
                stack.append(intervals2[i])
            # print(stack)
        
        return(stack)