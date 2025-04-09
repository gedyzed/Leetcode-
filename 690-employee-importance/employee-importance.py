"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(employee, visited):
    
            self.imp += employee.importance
            visited.add(employee.id)

            for id in employee.subordinates:
                if id not in visited:
                    visited.add(id)
                    dfs(graph[id], visited)

        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = employee

        self.imp = 0
        dfs(graph[id], set())
        return self.imp   
     
       
                 
   



        