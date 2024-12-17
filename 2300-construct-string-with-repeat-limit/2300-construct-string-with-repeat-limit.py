class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        print(freq)
        
        # stack = []
        # for i in freq:
        #     stack.append((i, freq[i]))
        
        # stack.sort(key=lambda x: x[0], reverse=False)

        # print(stack)

        # #[('a', 4), ('b', 3)], limit=2
        # # [('a', 1), ('c', 4), ('z', 2)], limit=3
        # ans=''
        # while(stack):
        #     letter, letterFreq = stack.pop()
            
        #     while(letterFreq>0):
        #         if(letterFreq<=repeatLimit):
        #             ans+=letter*letterFreq
        #             letterFreq-=letterFreq
        #         else:
        #             ans+=letter*repeatLimit
        #             letterFreq-=repeatLimit
        #             if(stack):
        #                 l2, f2 = stack.pop()
        #                 ans+=l2
        #                 f2-=1
        #                 if(f2>0):
        #                     stack.append((l2,f2))
        #             else:
        #                 return ans
        #                 print(ans)
        #                 break
        # return(ans)
        ###################################
        heap = []
        for i in freq:
            heapq.heappush(heap, (-ord(i), freq[i]))
        
        ans=''
        while(heap):
            l1, f1 = heapq.heappop(heap)
            ans+=chr(-l1) * min(repeatLimit, f1)
            f1-=repeatLimit

            if(f1>0):
                if(heap):
                    l2, f2 = heapq.heappop(heap)
                    ans+=chr(-l2)
                    f2-=1
                    if(f2>0):
                        heapq.heappush(heap, (l2, f2))
                else:
                    break
                
                heapq.heappush(heap, (l1, f1))
        print(ans)
        return ans
