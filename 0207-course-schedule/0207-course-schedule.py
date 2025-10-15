class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #topologic sort, bfs

        prereq_course = {}
        numberOfPrereq = {}
        completed_courses = set()
        
        for i in range(numCourses):
            numberOfPrereq[i] = 0
            prereq_course[i] = []
        
        for course, prereq in prerequisites:
            prereq_course[prereq].append(course)
            numberOfPrereq[course]+=1
        
        q = deque()

        for course in numberOfPrereq:
            if(numberOfPrereq[course]==0):
                q.append(course)
        
        while q:
            prereq = q.popleft()

            completed_courses.add(prereq)

            for c in prereq_course[prereq]:
                numberOfPrereq[c]-=1

                if(numberOfPrereq[c]==0):
                    q.append(c)
        
        return len(completed_courses)==numCourses