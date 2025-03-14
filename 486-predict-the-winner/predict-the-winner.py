class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def play(left, right):

            if left == right:
                return nums[left]
            
            left_sum = nums[left] - play(left + 1, right)
            right_sum = nums[right] - play(left, right - 1)

            return max(left_sum, right_sum)   

        return play(0, len(nums) - 1) >= 0     






         
        