class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack, area = [], 0
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                width = i
                if stack:
                    width = i - stack[-1] - 1
                
                area = max(area, heights[idx] * width)
            
            stack.append(i)
        
        return area

                    

            

        
        