class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(manager_, time):

            max_time = time
            for emp in graph[manager_]:
                max_time = max(max_time, dfs(emp, time + informTime[manager_]))

            return max_time       
                           
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)
        
       
        return dfs(headID, 0)      