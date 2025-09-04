class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        #t = d/s
        # return 1  else 2
        if abs(z-x)<abs(z-y):
            return 1
        elif(abs(z-x)==abs(z-y)):
            return 0
        else:
            return 2

