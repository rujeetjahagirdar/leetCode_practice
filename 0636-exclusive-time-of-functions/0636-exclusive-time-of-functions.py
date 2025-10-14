class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        #use stack to keep track of executions
        #if end log occurs, then it will definitely will be for function on top on execution stack

        #TC: O(n)
        #SC: O(ns)

        ans=[0]*n
        executionStack = [] #(function_id, start_time)

        for i in range(len(logs)):
            log = logs[i].split(":")
            f_id = int(log[0])
            operation = log[1]
            time = int(log[2])

            if(operation=='start'):
                if(not executionStack):
                    executionStack.append((f_id, time))
                else:
                    #stop previous function
                    #append this functino
                    ans[executionStack[-1][0]] += (time - executionStack[-1][1])
                    executionStack.append((f_id, time))
            else:
                #stop stack top function
                #pop stack top function
                ans[executionStack[-1][0]] += (time - executionStack[-1][1] +1)
                executionStack.pop()

                #if(is there is stopped function in executionStack, start it by updating its time to current time +1)
                if(executionStack):
                    executionStack[-1] = (executionStack[-1][0], time+1)
        return(ans)