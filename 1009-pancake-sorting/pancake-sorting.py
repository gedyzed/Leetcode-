class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        curr_size = len(arr)
        
        while curr_size > 1:
            k = self.findK(arr, curr_size)
            if k != curr_size - 1:
                if k != 0:  
                    flips.append(k + 1)
                    arr[:k + 1] = arr[:k + 1][::-1]
            
                flips.append(curr_size)
                arr[:curr_size] = arr[:curr_size][::-1]
            
            curr_size -= 1
        
        return flips

    def findK(self, arr: List[int], n: int) -> int:
        max_index = 0
        for i in range(1, n):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index
