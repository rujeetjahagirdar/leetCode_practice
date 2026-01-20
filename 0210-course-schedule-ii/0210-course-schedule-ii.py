class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #topologic sort, bfs

        #TC: O(numCourses + number of prerequisites)
        #SC: O(numCourses + number of prerequisites)

        prereq_course = {} #{prerequisite course -> course}
        numberOfPrereq = {} #{course -> no of prerequisite courses}
        # completed_courses = set()
        completed_courses = []
        
        for i in range(numCourses):
            numberOfPrereq[i] = 0
            prereq_course[i] = []
        
        for course, prereq in prerequisites:
            prereq_course[prereq].append(course)
            numberOfPrereq[course]+=1
        
        print(numberOfPrereq)
        print(prereq_course)

        q = deque()

        for course in numberOfPrereq:
            if(numberOfPrereq[course]==0):
                q.append(course)
        
        while q:                        # in this while loop, we are not processing prereq of every course,
            prereq = q.popleft()        # we are just processing prereq for the respective popped course, so
                                        # very prereq will be processed only once throughout whole execution 
            # completed_courses.add(prereq)
            completed_courses.append(prereq)

            for c in prereq_course[prereq]: #for every course which have current course as prepreq
                numberOfPrereq[c]-=1

                if(numberOfPrereq[c]==0):
                    q.append(c)
        
        print(completed_courses)
        if len(completed_courses)==numCourses:
            return completed_courses
        return []