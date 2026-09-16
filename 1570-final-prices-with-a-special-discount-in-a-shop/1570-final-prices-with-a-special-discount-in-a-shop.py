class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # ans=[0]*len(prices)
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if(prices[j]<=prices[i]):
        #             ans[i] = prices[i]-prices[j]
        #             break
        #         ans[i] = prices[i]
        # ans[-1] = prices[-1]
        # print(ans)
        # return ans

        #################
        # Approach 2: stack based
        # keep a stack of items for which discount can not be found
        #   we will push each element on the stack and as we progress from left to right we will pop the stack until stack top is less than current value and apply that discount

        no_discount_stack = []
        ans = [0]*len(prices)

        for i in range(len(prices)):
            while(no_discount_stack and prices[no_discount_stack[-1]]>=prices[i]):
                item_idx = no_discount_stack.pop()
                ans[item_idx]= prices[item_idx] - prices[i]

            no_discount_stack.append(i)
        
        print(no_discount_stack)
        print(ans)

        for i in no_discount_stack:
            ans[i] = prices[i]
        
        return(ans)