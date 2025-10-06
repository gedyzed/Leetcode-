class Solution:
    def countPrimes(self, n: int) -> int:
        def prime_sieve(n):

            isPrime = [True for _ in range(n + 1)]
            isPrime[0] = isPrime[1] = False

            i = 2
            while i <= n:
                if isPrime[i]:
                    j = 2 * i
                    while j <= n:
                        isPrime[j] = False
                        j += i
                i += 1

            return isPrime
            
        if n <= 1:
            return 0
        primes = prime_sieve(n)
        ans = 0
        for i, flag in enumerate(primes):
            if flag and n != i:
                ans += 1
      
        return ans 

        



                
         


            
        