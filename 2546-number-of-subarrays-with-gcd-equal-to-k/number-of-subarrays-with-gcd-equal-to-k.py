class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        n, count = len(nums), 0
        for i in range(n):
            gcd_ = nums[i]
            for j in range(i, n):
                gcd_ = gcd(gcd_, nums[j])
                if gcd_ == k:
                    count += 1
             
        return count 
        
        