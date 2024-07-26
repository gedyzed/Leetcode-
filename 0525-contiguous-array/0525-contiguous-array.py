class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        binary = {0 :-1}
        max_length, count = 0, 0 
        for i in range(len(nums)) :
            if nums[i] :
                count += 1
            else : 
                count -= 1

            if count in binary :
                max_length = max(max_length, i - binary[count])
            else :
                binary[count] = i
        return max_length

   











        