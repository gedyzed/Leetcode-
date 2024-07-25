class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        return self.merge_sort(nums)  

    def merge(self,left, right):
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        # Append remaining elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        
        return self.merge(left_half, right_half)
        
                 











        