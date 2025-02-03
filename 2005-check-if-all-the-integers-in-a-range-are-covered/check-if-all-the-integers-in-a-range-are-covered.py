class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        result = []
        for start, end in ranges:
            for num in range(start, end + 1):
                result.append(num)

        nums2 = set(result)
        nums1 = set([num for  num in range(left, right + 1)])        

        return nums1 <=  nums2



