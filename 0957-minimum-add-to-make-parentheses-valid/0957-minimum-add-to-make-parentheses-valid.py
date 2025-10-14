class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # #TC: O(n)
        # #SC: O(n)
        
        # unmatchedClosing = 0
        # stack=[]

        # for i in s:
        #     if(i=='('):
        #         stack.append(i)
        #     else:
        #         if(stack and stack[-1]=='('):
        #             stack.pop()
        #         else:
        #             unmatchedClosing+=1
        
        # return len(stack) + unmatchedClosing

        #############################


        openCounter=0
        unmatchedClosing=0

        for i in s:
            if(i=='('):
                openCounter+=1
            else:
                if(openCounter>0):
                    openCounter-=1
                else:
                    unmatchedClosing+=1
        
        return openCounter+unmatchedClosing