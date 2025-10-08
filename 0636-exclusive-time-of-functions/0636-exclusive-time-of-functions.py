class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        stack = []
        prev = 0

        for i in range(len(logs)):
            log = logs[i].split(":")
            f_id = int(log[0])
            ops = log[1]
            log_time = int(log[2])

            if(len(stack)==0):
                #assuming first will be start operation
                stack.append(f_id)
                prev = log_time
            else:
                if(ops=='start'):
                    #stop previous function
                    #update exclusive time for previous function
                    #update prev, time at which next function can start
                    #update stack

                    ans[stack[-1]]+=(log_time - prev)
                    prev = log_time
                    stack.append(f_id)

                elif(ops=='end'):
                    #update exclusive time for previous function
                    #pop from stack
                    #update prev, time at which next function can start

                    ans[stack[-1]]+= (log_time-prev+1)
                    prev = log_time+1
                    stack.pop()
        return(ans)
                