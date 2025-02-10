class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        height_name = dict(zip(heights, names))

        max_, min_ = max(heights), min(heights)
        countArray = [0] * (max_ - min_ + 1)

        for height in heights:
            countArray[max_ - height] += 1

        result = []  
        for i, count in enumerate(countArray):
            if count:
                result.extend([max_ - i] * count)  

        return [height_name[height] for height in result]     
