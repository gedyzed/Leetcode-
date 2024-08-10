class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)    
        self.presum = [0] * n
        for i in range(n):
            self.presum[i] = self.presum[i-1] + nums[i]
 
    def sumRange(self, left: int, right: int) -> int:   
        leftsum = self.presum[left-1] if left > 0 else 0
        rightsum = self.presum[right] 
        return rightsum - leftsum
    
    
      
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)