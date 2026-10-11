class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        pairs = []

        for i in range(1, int(area**0.5)+1):
            if(area%i==0):
                pairs.append([i, area//i])
        
        ans=[]
        mindiff=float("inf")


        for l, w in pairs:
            if(abs(l-w)<mindiff):
                ans = [max(l, w), min(l,w)]
        
        return ans