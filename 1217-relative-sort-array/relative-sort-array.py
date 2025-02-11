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

        arr.sort()

        result.extend(arr)
        return result