class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        nums1 = set([num for  num in range(left, right + 1)])
        result = []
        for start, end in ranges:
            for num in range(start, end + 1):
                result.append(num)
                
        nums2 = set(result)        

        return nums1 <=  nums2



