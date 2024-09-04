class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = 'N'
        points = []
        x, y = 0, 0
        obstacles2 = set(map(tuple, obstacles))
        # print([2,4] in obstacles)
        ans = float("-inf")
        for i in range(len(commands)):
            if (commands[i]==-1):
                if(direction =='N'):
                    direction = 'E'
                elif(direction =='E'):
                    direction = 'S'
                elif(direction =='S'):
                    direction = 'W'
                elif(direction =='W'):
                    direction = 'N'
            elif(commands[i]==-2):
                if(direction =='N'):
                    direction = 'W'
                elif(direction =='E'):
                    direction = 'N'
                elif(direction =='S'):
                    direction = 'E'
                elif(direction =='W'):
                    direction = 'S'
            else:
                if(direction=='N'):
                    for i in range(commands[i]):
                        if((x,y+1) not in obstacles2):
                            x = x
                            y = y+1
                    points.append([x,y])
                elif(direction=='E'):
                    for i in range(commands[i]):
                        if((x+1,y) not in obstacles2):
                            x = x+1
                            y = y
                    points.append([x,y])
                elif(direction=='S'):
                    for i in range(commands[i]):
                        if((x,y-1) not in obstacles2):
                            x = x
                            y = y-1
                    points.append([x,y])
                elif(direction=='W'):
                    for i in range(commands[i]):
                        if((x-1,y) not in obstacles2):
                            x = x-1
                            y = y
                    points.append([x,y])
                if(x**2 + y**2 > ans):
                    ans = x**2 + y**2
        print(points)
        print(x,y)
        print(direction)
        print(ans)
        return ans