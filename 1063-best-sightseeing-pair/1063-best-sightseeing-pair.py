class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # curr_max = values[0]
        # curr_max_index = 0
        # res=[]
        # # values = [8,1,5,2,6]
        # # [7,2,6,6,9,4,3]
        # for j in range(1, len(values)):
        #     res.append(values[j]+curr_max-(j-curr_max_index))

        #     if(values[j]>=curr_max):
        #         curr_max = values[j]
        #         curr_max_index = j
        
        # print(res)
        # return max(res)

        # #############

        # ans = float("-inf")

        # for i in range(len(values)-1):
        #     for j in range(i+1, len(values)):
        #         ans = max(ans, values[i]+values[j]-(j-i))
        # print(ans)
        # return ans

        ###############
        # [7,2,6,6,9,4,3]
        #socre = values[i] + values[j] -(j-i)
        #       = values[i] + i + values[j] - j
        
        maxLeftScore = [0]*len(values)
        maxLeftScore[0] = values[0]+0
        for i in range(1,len(values)):
            maxLeftScore[i] = max(maxLeftScore[i-1], values[i]+i)
        print(maxLeftScore)
        #[8, 8, 8, 8, 10]
        ans = 0

        for i in range(1, len(values)):
            ans = max(ans, maxLeftScore[i-1]+values[i]-i)

        print(ans)
        return ans