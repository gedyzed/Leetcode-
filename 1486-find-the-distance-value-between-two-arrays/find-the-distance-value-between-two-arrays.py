class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        for num1 in arr1:
            found = False
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    found = True

            if not found:
                count += 1

        return count                
        