class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums = {}
        answer = []
        stack = []

        for i in range(len(nums2)):
            nums[nums2[i]] = i

        for i in range(len(nums1)):
            found = False
            idx = nums[nums1[i]]
            while idx <= len(nums2)-1:
                if nums2[idx] > nums1[i]:
                    answer.append(nums2[idx])
                    found = True
                    break
                idx += 1 
            if not found :
                answer.append(-1)
                      
        return answer             







      



        