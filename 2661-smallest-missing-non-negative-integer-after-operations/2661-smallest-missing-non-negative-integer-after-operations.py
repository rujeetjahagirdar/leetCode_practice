class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        #bSearch
        # find (0+5*(n)), (1+5*(n)), (2+5*(n)), (3+5*(n)), .... in nums, if it does not exists, that is ans
        # range of n will be min(nums)//5 tot max(num)//5

        # nLower = -len(nums)#//value   #-2
        # nUpper = len(nums)#//value   #2
        # visited = set()

        # freq = Counter(nums)

        # for x in range(len(nums)+1): #??
        #     x_found = False
        #     if(x not in freq):
        #         for n in range(nLower, nUpper+1):
        #             print(x,n, x + (value * n))
        #             if(x + (value * n) in freq and freq[x + (value * n)]>0):
        #                 # visited.add(x + (value * n))
        #                 freq[x + (value * n)]-=1
        #                 x_found = True
        #                 break
        #         if(x_found==False):
        #             return x
        #         else:
        #             x_found = False
        #     else:
        #         freq[x]-=1
        #     print(x, freq)
            
        #     # print(visited)
        
        hashM = defaultdict(int)

        for n in nums:
            hashM[(n%value)]+=1
        
        for i in range(len(nums)+1):
            if(i%value in hashM):
                if(hashM[i%value]>0):
                    hashM[i%value]-=1
                else:
                    return i
            else:
                return i