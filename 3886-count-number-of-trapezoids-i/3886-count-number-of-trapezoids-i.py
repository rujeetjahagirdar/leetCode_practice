class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        points_be_height = defaultdict(int)

        for x, y in points:
            points_be_height[y]+=1
        
        # print(points_be_height)

        edges_by_height = defaultdict(int)

        for height in points_be_height:
            n = points_be_height[height]
            r = 2
            if(n>=2):
                # edges_by_height[height] = math.factorial(n) / (math.factorial(n-r) * math.factorial(r))  #nCr
                edges_by_height[height] = math.comb(n, r)
            # else:
            #     edges_by_height[height] = 0
        
        # print("edges: ", edges_by_height)

        if(not edges_by_height):
            return 0

        ans=0
        edges_by_height_val = list(edges_by_height.values())
        mod = 10**9 + 7
        
        # for i in range(len(edges_by_height_val)-1):
        #     for j in range(i+1, len(edges_by_height_val)):
        #         ans+=edges_by_height_val[i]*edges_by_height_val[j]
        
        # print(ans%mod)
        # return int(ans%mod) 

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