class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        def factorial(n):
            if n == 1 or not n:
                return 1
            return n * (n - 1)    
            
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                product[p] += 1 

        count = 0
        valid_tuples = [v for v in product.values() if v > 1] 
        num_fact = {}
        for tuples in valid_tuples:
            # if tuples not in num_fact:
            #     num_fact[tuples] = factorial(tuples)
            count += 4 * (tuples * (tuples - 1)) 
             
        return count    

        