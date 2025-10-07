class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {} #{prereq_course: [course1, course2, ....]}
        indegree = {} #{course: number of prereq courses}
        completed_courses = set()

        for i in range(numCourses):
            courses[i]=[]
            indegree[i]=0

        for course, prereq in prerequisites:
            courses[prereq].append(course)
            indegree[course]+=1
        
        q = deque()

        #find course with no prereq
        for c in indegree:
            if(indegree[c]==0):
                q.append(c)
        
        while q:
            c = q.popleft()

            #for all courses in which have c as prereq, reduce indegree by 1
            for curs in courses[c]:
                indegree[curs]-=1
                
                if indegree[curs]==0:
                    q.append(curs)
                
            completed_courses.add(c)
        
        return len(completed_courses)==numCourses
