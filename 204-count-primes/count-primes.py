class Solution:
    def countPrimes(self, n: int) -> int:
        def prime_sieve(n):

            isPrime = [True for _ in range(n + 1)]
            isPrime[0] = isPrime[1] = False

            for i in range(2, n + 1):
                if isPrime[i]:
                    for j in range(2 * i, n + 1, i):
                        isPrime[j] = False
                        
            return isPrime
            
        if n <= 1:
            return 0
        primes = prime_sieve(n)
        ans = 0
        for i, flag in enumerate(primes):
            if flag and n != i:
                ans += 1
      
        return ans 

        



                
         


            
        