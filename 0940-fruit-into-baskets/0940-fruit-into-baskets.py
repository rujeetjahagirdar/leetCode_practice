class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if(len(fruits)==1):
            return 1

        ans=float('-inf')

        # for i in range(len(fruits)-1):
        #     basket = set()
        #     basket.add(fruits[i])
        #     t=1
        #     for j in range(i+1, len(fruits)):
        #         if(fruits[j] in basket):
        #             t+=1
        #         elif(fruits[j] not in basket and len(basket)==1):
        #             basket.add(fruits[j])
        #             t+=1
        #         else:
        #             ans=max(ans, t)
        #             break
        #         # print(basket)
        #         ans=max(ans, t)
        # return(ans)
        ##################################
        # window = defaultdict(int)
        # ans=0

        # l=0

        # for r in range(len(fruits)):
        #     if(fruits[r] in window):
        #         window[fruits[r]]+=1
        #     elif(fruits[r] not in window and len(window)<2):
        #         window[fruits[r]]+=1
        #     else:
        #         window[fruits[r]]+=1

        #         while(len(window)>2):

        #             window[fruits[l]]-=1
    
        #             if(window[fruits[l]]==0):
        #                 del window[fruits[l]]
                    
        #             l+=1
        #     t = sum(window.values())
        #     ans=max(ans, t)
        # return(ans)
        #################################
        window = defaultdict(int)
        ans=0

        l=0

        for r in range(len(fruits)):
            window[fruits[r]]+=1

            while(len(window)>2):

                window[fruits[l]]-=1

                if(window[fruits[l]]==0):
                    del window[fruits[l]]
                
                l+=1
            t = (r-l)+1
            ans=max(ans, t)
        return(ans)