import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        ans = ''
        oddNums = []
        evenNums = []
        for i in str(num):
            if(int(i)%2==0):
                heapq.heappush(evenNums, -int(i))
            else:
                heapq.heappush(oddNums, -int(i))
        print(oddNums)
        print(evenNums)
        for i in str(num):
            if(int(i)%2==0):
                ans +=str(-heapq.heappop(evenNums))
            elif(int(i)%2!=0):
                ans +=str(-heapq.heappop(oddNums))
        print(ans)
        return int(ans)