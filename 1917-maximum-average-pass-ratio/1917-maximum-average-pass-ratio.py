class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #for each extra student, add this extra student to each class and check which class gives max ratio and select this class. repeat this process for next extra student # greddy approach



        

        # initial_ratios = []

        # for i in range(len(classes)):
        #     initial_ratios.append(classes[i][0]/classes[i][1])
        
        # print(initial_ratios)

        # while extraStudents>0:
        #     updated_ratios = []
        #     max_heap = []

        #     for i in range(len(classes)):
        #         updated_ratio = (classes[i][0]+1)/(classes[i][1]+1)
        #         increased_ratio = updated_ratios[i] - initial_ratios[i]
        #         heapq.heappush(max_heap, (-increased_ratio, i[0], i[1]))
            

        #     _, idx = heapq.heappop(max_heap)   
            
        #     initial_ratios[idx] = updated_ratios[idx]
        #     classes[idx] = [classes[idx][0]+1, classes[idx][1]+1]
        #     extraStudents -=1
        # print(initial_ratios)
        # ans = sum(initial_ratios)/len(initial_ratios)
        # print(ans)
        # return ans
############################
        max_heap = []

        ## Following part is not actually updating student counts for any class
        ## It is just to calculate POTENTIAL GAIN if first student is added to a class
        ## Pushing this gain to max_heap makes sure that the class with max gain will be on top
        for i in range(len(classes)):
            initial_ratio = (classes[i][0])/(classes[i][1])
            updated_ratio = (classes[i][0]+1)/(classes[i][1]+1)
            gain = updated_ratio - initial_ratio #POTENTIAL GAIN if first student is added to the clas
            heapq.heappush(max_heap, (-gain, classes[i][0], classes[i][1]))

        
        ## And in the following part we will actually iterate through extraStudents and update student counts.
        ## And we will calcualte new POENTIAL GAIN if next student is added to the class having current max gain
        for _ in range(extraStudents):
            currGain, passedStudents, totalStudents = heapq.heappop(max_heap) #
            
            passedStudents+=1
            totalStudents+=1
            currRatio = passedStudents/totalStudents
            newPotentialRatio = (passedStudents+1)/(totalStudents+1) #new potential ratio after adding next student

            newPotentialGain = newPotentialRatio - currRatio  #new POTENTIAL GAIN if next student is added to this class

            heapq.heappush(max_heap, (-newPotentialGain, passedStudents, totalStudents))
        print(max_heap)
        ans = 0

        for i in max_heap:
            ans += (i[1]/i[2])
        return(ans/len(max_heap))