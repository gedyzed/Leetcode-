class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeros,prod = 0,1
        ans = []
        for num in nums:
            if num : prod *= num
            else : zeros += 1

        for num in nums:
            if zeros :
                if zeros > 1 : ans.append(0)
                elif not num : ans.append(prod)    
                else : ans.append(0)   
            else : ans.append(int(prod/num))
        return ans          




