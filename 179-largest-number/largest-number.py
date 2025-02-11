class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def customComparator(n1, n2):

            if n1 + n2 > n2 + n1:
                return -1
            return 1        

        nums = list(map(str, nums))
        result = sorted(nums, key=cmp_to_key(customComparator)) 

        if result[0] == "0":
            return "0"      
        return "".join(result)    


            
        