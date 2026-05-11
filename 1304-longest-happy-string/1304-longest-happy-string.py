class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if(a>0):
            heapq.heappush(max_heap, (-a, 'a'))
        if(b>0):
            heapq.heappush(max_heap, (-b, 'b'))
        if(c>0):
            heapq.heappush(max_heap, (-c, 'c'))

        ans=''

        for i in range(a+b+c):
            cnt, ch = heapq.heappop(max_heap)
            cnt = -1*cnt
            if(len(ans)<2):
                ans+=ch
                cnt-=1

                if(cnt>0):
                    heapq.heappush(max_heap, (-cnt, ch))
            else:
                if(ch==ans[-1] and ch==ans[-2]):
                    if(max_heap):
                        cnt2, ch2 = heapq.heappop(max_heap)
                        cnt2 = -1*cnt2
                        ans+=ch2
                        cnt2-=1

                        if(cnt2>0):
                            heapq.heappush(max_heap, (-cnt2, ch2))
                        
                        if(cnt>0):
                            heapq.heappush(max_heap, (-cnt, ch))
                    else:
                        break
                else:
                    ans+=ch
                    cnt-=1

                    if(cnt>0):
                        heapq.heappush(max_heap, (-cnt, ch))
            print(ans)
        return ans
        

