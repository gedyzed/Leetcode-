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
    
            imp[0] += employee.importance
            visited.add(employee.id)

            for id in employee.subordinates:
                if id not in visited:
                    visited.add(id)
                    dfs(graph[id], visited)

        imp = [0]
        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = employee

        dfs(graph[id], set())
  
        return imp[0]   
     
       
                 
   



        