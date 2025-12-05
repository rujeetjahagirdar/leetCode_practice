class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        # maxRight = [0]*len(heights)
        # maxTill = len(heights)-1
        # for i in range(len(heights)-2, -1, -1):
        #     if(heights[i]<heights[i+1]):
        #         maxRight[i]=i+1
        #     else:
        #         maxRight[i]=maxTill
            
        #     if(heights[i]>=heights[maxTill]):
        #         maxTill=i
        
        # print(maxRight)
        # ans=[]

        # for i in range(len(heights)):
        #     ans.append(maxRight[i]-i)
        
        # print(ans)

        mono_stack = []
        ans=[0]*len(heights)

        for i in range(len(heights)-1, -1, -1):
            while(mono_stack and mono_stack[-1]<heights[i]):
                ans[i]+=1
                mono_stack.pop()
            
            if(mono_stack):
                ans[i]+=1

            mono_stack.append(heights[i])
            # print(mono_stack)
        print(ans)

        return ans