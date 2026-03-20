class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        #traverse kxk matrixes
        #sort elements in those matrix and find min diff elements
        ans=[]

        for i in range(len(grid)-k +1):
            t = []
            for j in range(len(grid[0])-k +1):
                elements = []
                # print(f"i={i}, j={j}")
                for x in range(k):
                    for y in range(k):
                        # print(f"x= {x}, y={y}")
                        elements.append(grid[i+x][j+y])
                # print(elements)
                elements.sort()
                m_diff = float("inf")
                for e in range(len(elements)-1):
                    if(elements[e]!=elements[e+1]):
                        m_diff = min(m_diff, abs(elements[e]-elements[e+1]))
                if(m_diff==float("inf")):
                    m_diff=0
                t.append(m_diff)

            ans.append(t)
        
        # print(ans)

        return ans
                