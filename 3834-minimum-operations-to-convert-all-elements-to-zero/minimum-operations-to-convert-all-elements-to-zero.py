class Solution:
    def minOperations(self, nums: List[int]) -> int:

        stack = []
        count = 0
        for num in nums:
            popped = set()
            while stack and stack[-1] > num:
                popped.add(stack.pop())
            count += len(popped)
            stack.append(num)

        for num in list(set(stack)):
            if num:
                count += 1

        return count 
        
        