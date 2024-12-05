class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        #minHeap1
        #minHeap2

        #if len costs greater than or eqauals 2*candiadtes  
            # make to min heaps
        #else:
            #make one heap
        #for k sessions:
            #check min from both heaps
                #if they are same extract from first heap
                #if first heap length<candiadte
                    #if have remaining candidates
                        #add remaining candiadte form original to this heap
                    #else
                        #add all elements from this heap(heap with less candidates) to other heap\\\\

        i=0
        j=len(costs)-1
        minHeap1=[]
        minHeap2=[]

        if(len(costs)>=2*candidates):
            while(i<=candidates-1):
                heapq.heappush(minHeap1, (costs[i], i))
                i+=1
            while(j>=len(costs)-candidates):
                heapq.heappush(minHeap2, (costs[j], j))
                j-=1
            i-=1
            j+=1

        else:
            while(i<len(costs)):
                heapq.heappush(minHeap1, (costs[i], i))
                i+=1
            i-=1
        
        print(minHeap1)
        print(minHeap2)


        ans=0
        for _ in range(k):
            if(len(minHeap2)!=0):
                if(minHeap1 and (minHeap1[0]<=minHeap2[0])):
                    ans+=heapq.heappop(minHeap1)[0]

                    if (j-i)>1:
                        i += 1
                        heapq.heappush(minHeap1, (costs[i], i))
                        
                else:
                    ans+=heapq.heappop(minHeap2)[0]

                    if (j-i)>1:
                        j-=1
                        heapq.heappush(minHeap2, (costs[j], j))
                        # j -= 1
            else:
                ans+=heapq.heappop(minHeap1)[0]

                if (j-i)>1:
                    i += 1
                    heapq.heappush(minHeap1, (costs[i], i))
                    # i += 1      
        print(ans)          
        return ans