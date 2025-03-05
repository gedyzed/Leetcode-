class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
       
        value_num = defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                value = stack.pop()
                value_num[value] = i - value[0]
                
            stack.append((i, temp))  

        return [value_num[(i, temp)] if value_num[(i, temp)] else 0 for i, temp in enumerate(temperatures)]       

        