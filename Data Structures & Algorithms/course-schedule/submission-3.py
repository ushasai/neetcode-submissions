class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {}
        path = set()
        done = set()
        graph = defaultdict(list)
        for c,p in prerequisites :
            graph[c].append(p)

        def dfs(course):

            if course in path:
                return False
            if course in done:
                return True
            path.add(course)
            for p in graph[course]:
                if not dfs(p):
                    return False
            path.remove(course)
            done.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
                

                
            
            
        g                    




        

        