class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        
        # two pointers
        self.rear = self.front = -1
        self.count = 0
        
    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
    
        if self.isEmpty():
            self.rear = self.front = 0
        else:
            self.front = (self.front - 1) % self.k

        self.queue[self.front] = value
        self.count += 1  
        return True    

    def insertLast(self, value: int) -> bool:

        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
          
        self.queue[self.rear] = value  
        self.count += 1 
        return True    

    def deleteFront(self) -> bool:

        if self.isEmpty():
            return False

        if self.count == 1:
            self.front = self.rear = -1
        else:    
            self.front = (self.front + 1 ) % self.k

        self.count -= 1
        return True    

    def deleteLast(self) -> bool:

        if self.isEmpty():
            return False

        if self.count == 1:
            self.rear = self.front = -1
        else:        
            self.rear = (self.rear - 1) % self.k  

        self.count -= 1
        return True
        
    def getFront(self) -> int:

        if self.isEmpty():
            return -1
        return self.queue[self.front]    

    def getRear(self) -> int:

        if self.isEmpty():
            return -1
        return self.queue[self.rear]    
        
    def isEmpty(self) -> bool:
        return not self.count
    
    def isFull(self) -> bool:
        return self.count == self.k    
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()