class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left, right = [], [] 
        count = 0
        for num in nums:

            if num == pivot:
                count += 1
            elif num < pivot:
                left.append(num) 
            else:
                right.append(num)

        left.extend([pivot] * count)
        left.extend(right)  

        return left
                
