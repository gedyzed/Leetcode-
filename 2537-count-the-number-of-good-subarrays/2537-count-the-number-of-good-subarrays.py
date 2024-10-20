class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        numbers = defaultdict(int)
        counter = left = 0
        good_array = 0

        for right in range(len(nums)):
            counter += numbers[nums[right]]
            numbers[nums[right]] += 1
   
            while counter >= k:
                good_array += len(nums) - right
                numbers[nums[left]] -= 1
                counter -= numbers[nums[left]]
                left += 1

        return good_array            
                    


            


           

        
        