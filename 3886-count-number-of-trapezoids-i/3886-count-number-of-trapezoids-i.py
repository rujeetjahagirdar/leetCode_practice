class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        #combination of every edge on a particular y level with every other edges on different y levels

        #count x points at every y level
        points_by_height = defaultdict(int)
        for x, y in points:
            points_by_height[y]+=1
        
        #number of edges that can be formed at each y level
        edges_by_height = defaultdict(int)
        for height in points_by_height:
            n = points_by_height[height]
            r = 2
            if(n>=2):
                #nCr
                edges_by_height[height] = math.comb(n, r)
        
        # print("edges: ", edges_by_height)

        if(not edges_by_height):
            return 0


        ans=0
        edges_by_height_val = list(edges_by_height.values())
        mod = 10**9 + 7

        prefixSumRight = [-1]*len(edges_by_height_val)
        cummSum = 0

        for i in range(len(edges_by_height_val)-1, -1, -1):
            cummSum+=edges_by_height_val[i]
            prefixSumRight[i]=cummSum
        
        print(prefixSumRight)

        for i in range(len(edges_by_height_val)):
            sum_right = prefixSumRight[i] - edges_by_height_val[i]
            ans+=(sum_right * edges_by_height_val[i])

        print(ans%mod)
        return int(ans%mod) 