from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if len(courses[course]) == 0:
                return True
            
            visit.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            courses[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
