class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        stack = [i+1 for i in range(n)]
        visited = set()
        ans=[-1]*(2*(n-1)+1)
        print(len(ans))
        print(stack)

        
        #[5,4,3,2,1]
        #[-1,-1,-1,-1,-1,-1,-1,-1, -1]
        
        def backtrack(idx):

            if(idx==len(ans)):
                return True

            if(ans[idx]!=-1):
                return backtrack(idx+1)

            for i in reversed(range(1, n+1)):
                if(i not in visited):
                    if(i==1):
                        if(ans[idx]==-1):
                            ans[idx]=1
                            visited.add(1)
                            if(backtrack(idx+1)):
                                return True
                            else:
                                ans[idx]=-1
                                visited.remove(1)
                    else:
                        if(idx+i<len(ans) and ans[idx]==-1 and ans[idx+i]==-1):
                            ans[idx]=i
                            ans[idx+i]=i
                            visited.add(i)
                            if(backtrack(idx+1)):
                                return True
                            else:
                                ans[idx]=-1
                                ans[idx+i]=-1
                                visited.remove(i)
                        else:
                            pass
        
        backtrack(0)
        print(ans)
        return ans


#########################################################
        # # stack = [1,2,3]
        # # ans = [-1,-1,-1,-1,-1]
        # for i in range(len(ans)):
        #     while(stack):
        #         n = stack.pop(-1)
        #         print(stack)
        #         if(n!=1):
        #             if(ans[i]==-1 and ans[i+n]==-1):
        #                 ans[i]=n
        #                 ans[i+n]=n
        #                 print(ans)
        #                 if(len(temp)>0):
        #                     while(temp):
        #                         stack.append(temp.pop(-1))
        #                         print(stack)
        #                 break
        #             else:
        #                 temp.append(n)
        #                 print(temp)
        #         else:
        #             if(ans[i]==-1):
        #                 ans[i]=n
        #                 print(ans)
        #                 if(len(temp)>0):
        #                     while(temp):
        #                         stack.append(temp.pop(-1))
        #                         print(ans)
        #                 break
        #             else:
        #                 temp.append(n)
        #                 print(temp)
        #     # print(stack)
        #     # print(temp)
        #     # print(ans)
