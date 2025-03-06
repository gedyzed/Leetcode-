class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack, n = [], len(temperatures)
        value_num = defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                value = stack.pop()
                value_num[value] = i - value
                
            stack.append(i)  

        return [value_num[i] if value_num[i] else 0 for i in range(n)]       

        