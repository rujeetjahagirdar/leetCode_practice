class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes_with_balls = []
        ans=[]
        for i in range(len(boxes)):
            if(boxes[i]=='1'):
                boxes_with_balls.append(i)
        print(boxes_with_balls)

        for i in range(len(boxes)):
            moves=0
            for j in boxes_with_balls:
                if(i!=j):
                    moves+=abs(j-i)
            ans.append(moves)
        print(ans)
        return ans