class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack, n = [], len(temperatures)
        daily_temp = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                daily_temp[idx] = i - idx
                
            stack.append(i)  

        return daily_temp      

        