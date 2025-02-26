class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #process most frequent tasks first
        #if task freq is reamining, that that task to waiting queue
            #when witing time of tha task in waiting queue is reached add it to heap
        

        max_heap = []

        c = Counter(tasks)

        ans = []

        for t in c:
            heapq.heappush(max_heap, (-c[t], t))
        
        print(max_heap)

        waitingQueue = deque()
        currTime=0

        while (max_heap or waitingQueue):
            currTime+=1
            if(len(max_heap)>0):
                f, t = heapq.heappop(max_heap)
            
                f=-f

                ans.append(t)
                f-=1

                if(f>0):
                    waitingQueue.append((f, t, currTime+n))
            
            else: #if all tasks are in waiting queue(idle)
                ans.append("_")
            
            if(waitingQueue):
                if(currTime>=waitingQueue[0][2]): #if task in waiting queue is ready to be processed
                    iF, iT, iTime = waitingQueue.popleft()
                    heapq.heappush(max_heap, (-iF, iT))
            
            # print(ans)
        return currTime