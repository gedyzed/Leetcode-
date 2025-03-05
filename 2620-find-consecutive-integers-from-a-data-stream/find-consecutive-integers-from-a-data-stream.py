class DataStream:

    def __init__(self, value: int, k: int):

        self.queue = deque()
        self.k = k 
        self.value = value

    def consec(self, num: int) -> bool:

        if num != self.value:
            self.queue = deque()
            return False

        self.queue.append(num)
        return len(self.queue) >= self.k      


           
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)