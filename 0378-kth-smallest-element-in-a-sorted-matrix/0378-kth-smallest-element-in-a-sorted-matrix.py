class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        min_heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if(len(min_heap)==k):
                #     if(matrix[i][j]<min_heap[-1]):
                #         heapq.heappush(min_heap, matrix[i][j])
                #         print(min_heap)
                #         min_heap.pop()
                #         print(min_heap)
                #         heapq.heapify(min_heap)
                # else:
                #     heapq.heappush(min_heap, matrix[i][j])
                # print(min_heap)
                # heapq.heappush(min_heap, matrix[i][j])
                bisect.insort(min_heap, matrix[i][j])
                # print(min_heap)
                while(len(min_heap)>k):
                    min_heap.pop()
                    # heapq.heapify(min_heap)
        
        return(min_heap[-1])
        