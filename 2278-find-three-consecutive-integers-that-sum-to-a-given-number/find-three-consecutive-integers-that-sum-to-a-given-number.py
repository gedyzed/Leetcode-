class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        middle = num // 3
        prev, next = middle - 1, middle + 1
        if (prev + middle + next) == num:
            return [prev, middle, next]   
        elif (middle + 2 * next + 1 ) == num:
            return [middle, next, next + 1 ]   
        elif (prev * 2  + middle - 1 ) == num:
             return [prev - 1 , prev, middle ]   
          
        return []      

        