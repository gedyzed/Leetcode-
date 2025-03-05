class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        value_num = defaultdict(int)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                value = stack.pop()
                value_num[value] = num

            stack.append(num)

        return [value_num[num] if value_num[num] else -1  for num in nums1 ]       
 
        