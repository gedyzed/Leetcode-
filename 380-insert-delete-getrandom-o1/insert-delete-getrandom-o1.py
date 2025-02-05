class RandomizedSet:

    def __init__(self):
        self.index_value = {}
        self.value = []
        
    def insert(self, val: int) -> bool:

        if val in self.index_value:
            return False

        idx = len(self.value)
        self.index_value[val] = idx
        self.value.append(val)
        return True    
        
    def remove(self, val: int) -> bool:

        if val not in self.index_value:
            return False

        idx = self.index_value[val]
        self.index_value[self.value[-1]] = idx
        self.value[idx], self.value[-1] = self.value[-1], self.value[idx]
        self.value.pop()
        del self.index_value[val]
        return True

    def getRandom(self) -> int:

        idx = random.randint(0, len(self.value) - 1)
        return self.value[idx]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()