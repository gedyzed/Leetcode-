class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #  removing duplicates
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        left = 0
        right = min(len(nums1),len(nums2))
        answer = []

        while left < right:
            if right == len(nums1):
                if nums1[left] in nums2:
                    answer.append(nums1[left])
            else:
                if nums2[left] in nums1:
                    answer.append(nums2[left])   
            left += 1    
        return answer    



        