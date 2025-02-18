class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        val_index = {}
        for row in range(len(score)):
            val_index[score[row][k]] = row

        val_index = dict(sorted(val_index.items(), key=lambda item : item[0], reverse=True)) 
    
        result = []
        for idx in val_index.values():
            result.append(score[idx])  

        return result    

        