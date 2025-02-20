class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.prefix = 1
        
    def add(self, num: int) -> None:

        if not num:
           self.product = [1]
        else:
            val = self.product[-1]
            self.product.append(val * num)     
         
    def getProduct(self, k: int) -> int:

        if k >= len(self.product):
            return 0
        return self.product[-1] // self.product[- k - 1]
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)