class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ans=[]

        
        def find_index(a, i):
            l, r = 0, len(a)

            while(l<r):
                mid = (l+r)//2

                if(a[mid]<i):
                    l = mid+1
                else:
                    r = mid
            
            return l
        
        if(x<=arr[0]):
            return arr[:k]
        elif(x>=arr[-1]):
            return arr[-k:]
        
        else:
            idx = find_index(arr, x)
            print(x, idx)

            l, r = idx-1, idx

            while(len(ans)<k):
                if(l>=0 and r<len(arr)):
                    l_diff = abs(arr[l]-x)
                    r_diff = abs(arr[r]-x)
                    if(l_diff<=r_diff):
                        ans.append(arr[l])
                        l-=1
                    elif(l_diff>r_diff):
                        ans.append(arr[r])
                        r+=1
                   
                if(l<0):
                    while(len(ans)<k):
                        ans.append(arr[r])
                        r+=1
                if(r>=len(arr)):
                    while(len(ans)<k):
                        ans.append(arr[l])
                        l-=1
        ans.sort()
        return(ans)
