class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def checker(num):
            single = num // a + num // b + num // c
            double = num //lcm(a,  b) +  num // lcm(a, c) + num // lcm(b, c)
            triple = num // lcm(a, lcm(b, c))

            total = single - double  + triple
            return total

        low, high = 1, 2 * 10**9
        while low < high:
            mid = (low + high) // 2
            if checker(mid) < n:
                low = mid + 1
            else:
                high = mid
                
        return low
            
      