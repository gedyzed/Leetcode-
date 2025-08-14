class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_num,  left = -1, 0
        ans = ""
        for r in range(1, len(num)):
            if num[r] != num[r - 1] or num[r] != num[left]:
                left += 1
            
            if r - left + 1 == 3:
                new_num = num[left: r + 1]
                if max_num < int(new_num):
                    max_num = int(new_num)
                    ans = new_num
                left += 1  
        
        return ans


            
        