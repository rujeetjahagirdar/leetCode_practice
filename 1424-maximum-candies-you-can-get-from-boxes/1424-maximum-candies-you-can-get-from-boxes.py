class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        ans=0
        
        for b in initialBoxes:
            q.append(b)
        
        hasKeys = set()
        hasBox = set()

        while(q):
            box = q.popleft()

            if(candies[box]>0 and status[box]==1):
                ans+=candies[box]
                candies[box]=0
                for k in keys[box]:
                    hasKeys.add(k)
                for b in containedBoxes[box]:
                    q.append(b)

            else:
                hasBox.add(box)
            
            if(hasKeys):
                for k in hasKeys:
                    if(k in hasBox):
                        status[k]=1
                        q.append(k)
                        hasBox.remove(k)

        return(ans)

        