class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]   # one empty list per course
        for course, pre in prerequisites:          # unpack each pair
            graph[course].append(pre)
        seen = set()
        done = set()
        order = []
        def dfs(node):
            if node in done:
                return True
            if node in seen:
                return False
            seen.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            done.add(node)
            seen.remove(node)
            order.append(node)
            return order
        for c in range(numCourses):
            if not dfs(c):
                return []
        return order

                
            
        
        