class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr1_count = Counter(arr1)
        arr2_count = defaultdict(int)
        result = []
        for num in arr2:
            result.extend([num] * arr1_count[num])
            arr2_count[num] += 1     

        arr = []
        for num in arr1:
            if num not in arr2_count:
                arr.append(num)

        if len(arr) > 1:
            max_, min_ = max(arr), min(arr)  
            countArray = [0] * (max_ - min_ + 1)     
            for num in arr:
                countArray[num - min_] += 1

            sorted_arr = [] 
            for i, count in enumerate(countArray):
                if count:
                    sorted_arr.extend([i + min_] * count)   

            result.extend(sorted_arr)
            
        return result