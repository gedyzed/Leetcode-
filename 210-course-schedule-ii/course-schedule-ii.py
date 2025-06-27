class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        incoming = defaultdict(int)

        for a, b in prerequisites:
            graph[a].append(b)
            incoming[b] += 1 

        print(incoming)    

        queue = deque([node for node in range(numCourses) if not incoming[node]])
        ans = []
        while queue:
            node = queue.popleft()  
            ans.append(node) 
            for nei in graph[node]:
                incoming[nei] -= 1
                if not incoming[nei]:
                    queue.append(nei)
        
        return ans[::-1] if len(ans) == numCourses else []               

           