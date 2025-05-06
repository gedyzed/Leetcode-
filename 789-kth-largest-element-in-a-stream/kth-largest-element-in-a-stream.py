class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nlargest(k, nums)
        self.heap = []
        for num in self.nums:
            heappush(self.heap, num)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
            
        elif self.heap and val >= self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)

        return self.heap[0] if len(self.heap) == self.k else None    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)