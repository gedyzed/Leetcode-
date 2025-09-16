class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        ans = [] 
        for num in nums:
            ans.append(num)
            while len(ans) > 1:
                hcf = gcd(ans[-1], ans[-2])
                if hcf == 1:
                    break
                lcm = (ans[-1] * ans[-2]) // hcf
                ans.pop()
                ans.pop()
                ans.append(lcm)    
                    
        return ans        
                






        