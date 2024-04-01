class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        #create two pointers left and right
        left = 0   # points to the first element
        right = 1 # points to the second element

        counter = 0 # initialize counter

        for i in range(len(nums)):
           for j in range(1,len(nums)):
               if i < j: 
                    if nums[i] == nums[j] and i*j % k == 0:
                         counter += 1
        return counter        



