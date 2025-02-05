class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        result, evens_sum = [], 0
        for num in nums:
            if num % 2 == 0:
                evens_sum += num
                
        for value, index in queries:
            num = nums[index] + value

            if num % 2 == 0 :
                if nums[index] % 2 != 0:
                    evens_sum += num
                else:
                    evens_sum += num - nums[index] 
                    
            elif num % 2 != 0 and nums[index] % 2 == 0:
                evens_sum -= nums[index] 

            nums[index] = num           
            result.append(evens_sum)        

        return result        




        