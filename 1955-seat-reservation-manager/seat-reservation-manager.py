class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.un = []
        for i in range(1, n + 1):
            heappush(self.un, i)
        
    def reserve(self) -> int:
        val = heappop(self.un)
        heappush(self.heap, val)
        return val

    def unreserve(self, seatNumber: int) -> None:

        seats = []
        while seatNumber != self.heap[0]:
            seats.append(heappop(self.heap))
        val = heappop(self.heap)   
        heappush(self.un, val)    
        while seats:
            heappush(self.heap, seats.pop())

 
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)