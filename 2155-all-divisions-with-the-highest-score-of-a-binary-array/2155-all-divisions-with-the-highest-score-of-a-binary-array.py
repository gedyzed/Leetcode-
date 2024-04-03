class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones,scores  = 0,[]  # ones stores whole number of one in the array
        score,maxScore = 0,0 # score -> stores each scores instance ,maxScore ->stores the maximum score
        countOnes,countZeros = 0,0 # stores the number of ones and zeros on the left side
        
        for num in nums:
            if num:
                ones += 1
        zeros = len(nums)-ones   # stores whole number of zeros in the array

        for i in range(-1,len(nums)) :
            if i == -1:
                score = ones
                scores.append(score)   
            elif i == len(nums)-1:
                score = zeros
                scores.append(score)
            else: 
                if nums[i]:
                    countOnes += 1 # counts one on the left side
                else :
                    countZeros += 1 # counts zero on the right side
                rightones = ones - countOnes   # calculates ones on the right side    
                score = countZeros + rightones
                scores.append(score)    
            if maxScore < score:
                maxScore = score
        answer = []    
        for i in range(len(scores)):
            if scores[i] == maxScore:
                answer.append(i)  
        return answer  
