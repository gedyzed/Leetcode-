class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:   
            answer.extend(str(num))
        return [int(num) for num in answer]    

        