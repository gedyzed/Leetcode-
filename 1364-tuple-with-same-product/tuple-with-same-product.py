class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
           
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                product[p] += 1 

        count = 0
        # valid_tuples = [v for v in product.values() if v > 1] 
        for tuples in product.values():
            if tuples > 1:
                count += 4 * (tuples * (tuples - 1)) 
             
        return count    

        