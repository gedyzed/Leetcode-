class Solution:
    def trailingZeroes(self, n: int) -> int:

        def factorial(n):

            if n == 1 or n == 0:
                return 1
            return n * factorial(n - 1)    

        fact, count = factorial(n), 0 
        while not fact % 10:
            count += 1
            fact //= 10

        return count     

        