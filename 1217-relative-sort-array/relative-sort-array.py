class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        count = Counter(arr1)
        arr,ans = [], [] 
        left = right = 0
        for num in arr1:
            if num not in arr2:
                arr.append(num)
        arr.sort()        

        while left < len(arr2):
            if count[arr2[left]] > 0:
                ans.append(arr2[left]) 
                count[arr2[left]] -= 1
            else: left += 1 

        ans.extend(arr)
              
        return ans
        