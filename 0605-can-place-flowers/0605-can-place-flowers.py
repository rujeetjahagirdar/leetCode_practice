class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # if(n==0):
        #     return True

        for i in range(len(flowerbed)):
            if(flowerbed[i]==0):
                if(i==0 or flowerbed[i-1]==0):
                    left=True
                else:
                    left=False
                if(i==len(flowerbed)-1 or flowerbed[i+1]==0):
                    right = True
                else:
                    right=False
                
                if(left and right):
                    flowerbed[i]=1
                    n-=1
                
                if(n<=0):
                    return True
        return n==0
