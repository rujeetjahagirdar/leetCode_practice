class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {} #{prereq: [course1, course2, .....]}
        prereq_counts = {} #{course1:0, course2:0, .....}
        completed_courses = set()

        if(len(prerequisites)==0):
            return True

        for i in range(numCourses):
            courses[i] = []
            prereq_counts[i] = 0
        
        for course, prereq in prerequisites:
            courses[prereq].append(course)
            prereq_counts[course]+=1
        
        q = deque()

        for c in prereq_counts:
            if(prereq_counts[c]==0):
                q.append(c)
                completed_courses.add(c)
        
        while q:
            prereq = q.popleft()

            for c in courses[prereq]:
                prereq_counts[c]-=1

                if(prereq_counts[c]==0):
                    q.append(c)
                    completed_courses.add(c)
        
        return len(completed_courses)==numCourses



        
        #====================================================

        # #TC: O(number of courses + number of prereq)
        # #SC: O(number of courses + number of prereq)

        # prereq_mapping = {}

        # for i in range(numCourses):
        #     prereq_mapping[i] = set()

        # if(len(prerequisites)==0):
        #     return True

        # for course, prereq in prerequisites:
        #     prereq_mapping[prereq].add(course)
           
        # print(prereq_mapping)
        
        # q = deque()
        # completed_courses = set()

        # for course in prereq_mapping:
        #     if(len(prereq_mapping[course])==0):
        #         q.append(course)
        #         completed_courses.add(course)
        
        # while q:
        #     course = q.popleft()

        #     for c in prereq_mapping:
        #         if(course in prereq_mapping[c]): #O(number of courses + number of prereq)
        #             prereq_mapping[c].remove(course)

        #             if(len(prereq_mapping[c])==0):
        #                 q.append(c)
        #                 completed_courses.add(c)

        # print(len(completed_courses))    
        # return len(completed_courses)==numCourses