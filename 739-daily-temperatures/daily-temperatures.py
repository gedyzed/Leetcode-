class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack, n = [], len(temperatures)
        value_num = defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                value = stack.pop()
                value_num[value[0]] = i - value[0]
                
            stack.append((i, temp))  

        return [value_num[i] if value_num[i] else 0 for i in range(n)]       

        