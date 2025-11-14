# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #for all directions in clockwise [up, right, down, left]
            #try to move and clean using dfs
        #after trying all directions, backtrack to previous cell and continue in remaining directions


        def dfs(i, j, current_direction, visited):
            #clean
            #add visited
            #calculate new i,j based on directoin for all directions
            #call dfs recursively
            #backrack

            robot.clean()
            visited.add((i, j))


            for d in range(4):
                new_direction = (current_direction + d)%4
                newi, newj = i+directions[new_direction][0], j+directions[new_direction][1]

                if(newi, newj) not in visited and robot.move():
                    dfs(newi, newj, new_direction, visited)

                    #backtrack
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                

                robot.turnRight()

            




        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        dfs(0, 0, 0, visited)

        