class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks_ = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        indexed_task = sorted(tasks_)
        heap, res = [], []
        time = i = 0 

        while i < len(tasks) or heap:

            if not heap and indexed_task[i][0] > time:
                time = indexed_task[i][0]

            while i < len(tasks) and indexed_task[i][0] <= time:
                en, pt, index = indexed_task[i]  
                heappush(heap, (pt, index))
                i += 1

            if heap:
                pt, index = heappop(heap)
                time += pt
                res.append(index)    

        return res        


        

       
                  