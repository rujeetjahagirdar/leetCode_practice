class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq_mapping = {}

        for i in range(numCourses):
            prereq_mapping[i] = set()

        if(len(prerequisites)==0):
            return True

        for course, prereq in prerequisites:
            prereq_mapping[prereq].add(course)
           
        print(prereq_mapping)
        
        q = deque()
        completed_courses = set()

        for course in prereq_mapping:
            if(len(prereq_mapping[course])==0):
                q.append(course)
                completed_courses.add(course)
        
        while q:
            course = q.popleft()

            for c in prereq_mapping:
                if(course in prereq_mapping[c]):
                    prereq_mapping[c].remove(course)

                    if(len(prereq_mapping[c])==0):
                        q.append(c)
                        completed_courses.add(c)

        print(len(completed_courses))    
        return len(completed_courses)==numCourses
        

        