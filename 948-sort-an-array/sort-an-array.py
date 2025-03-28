class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_half,right_half) -> List[int]:
            left, right = 0, 0
            merged = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    merged.append(left_half[left])
                    left += 1
                else:
                    merged.append(right_half[right])
                    right += 1
            
            merged.extend(left_half[left:])
            merged.extend(right_half[right:])

            return merged

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            
            idx = (left + right) // 2
            left_half = mergeSort(left, idx, arr)
            right_half = mergeSort(idx + 1, right, arr) 
            
            return merge(left_half, right_half)

        return mergeSort(0, len(nums) - 1, nums)    

 

        