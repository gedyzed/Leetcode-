class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        incoming = defaultdict(int)
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        queue = deque()
        res = []

        for course in range(numCourses):
            if not incoming[course]:
                queue.append(course)

        while queue:
            course = queue.popleft()
            res.append(course)

            for nei in graph[course]:
                incoming[nei] -= 1
                if not incoming[nei]:
                    queue.append(nei)
                    
        if len(res) == numCourses:
            return res

        return []                





   


        