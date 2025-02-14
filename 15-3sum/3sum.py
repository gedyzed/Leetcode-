class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res1 = set()
        res2 = []
        nums.sort()
        for i in range(len(nums)-2):
            j ,k= i+1, len(nums)-1

            while j <k :
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    if (nums[i],nums[j] , nums[k]) not in res1:
                        res1.add((nums[i],nums[j] , nums[k]))
                        res2.append([nums[i],nums[j] , nums[k]])
                    j+=1
                    k-=1
                elif temp > 0:
                    k-=1
                else:
                    j+=1
        
        return res2
