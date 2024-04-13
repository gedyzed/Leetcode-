class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = 0
        right = len(letters)-1
 

        while left <= right :
            mid = (left + right)//2
            if letters[mid] == target and mid + 1 <= len(letters)-1 and  letters[mid+1] != target:   
                return letters[mid+1]
            elif letters[mid] > target and  mid-1 >= 0 and letters[mid-1] <= target :   
                return letters[mid]   
            elif letters[mid] > target :
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[0]            

        