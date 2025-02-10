class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        height_name = {}
        for i in range(len(names)):
            height_name[heights[i]] = names[i]

        for i in range(len(names)):
            is_sorted = True
            for j in range(1, len(names)):
                if heights[j - 1] < heights[j]:
                    heights[j - 1], heights[j] = heights[j], heights[j - 1]
                    is_sorted = False
                    
            if is_sorted:
                break        

        return [height_name[height] for height in heights]          

        