class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        visited = set()
        ans=[-1]*(2*(n-1)+1)

        
        #[5,4,3,2,1]
        #[-1,-1,-1,-1,-1,-1,-1,-1, -1]
        # for each index of ans
            #we will try all the values in range n to 1 meeting the condition.
            # then we will try to fill next index+1 of ans, if that is not successfull, we will revert the index changes
        
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
                            # print("Visisted: ",visited)
                            # print(ans)                        
                            if(backtrack(idx+1)):
                                return True
                            else:
                                ans[idx]=-1
                                visited.remove(1)
                                # print("Visisted: ",visited)
                                # print(ans)
                                
                    else:
                        if(idx+i<len(ans) and ans[idx]==-1 and ans[idx+i]==-1):
                            ans[idx]=i
                            ans[idx+i]=i
                            visited.add(i)
                            # print("Visisted: ",visited)
                            # print(ans)
                            if(backtrack(idx+1)):
                                return True
                            else:
                                ans[idx]=-1
                                ans[idx+i]=-1
                                visited.remove(i)
                                # print("Visisted: ",visited)
                                # print(ans) 
                                # return False
                        else:
                            pass
            return False
        
        if(backtrack(0)):
            print(ans)
            return ans


#########################################################