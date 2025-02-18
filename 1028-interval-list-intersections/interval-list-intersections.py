class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        left = right = 0
        result = []
        max_ = -1
        while left < len(firstList) and right < len(secondList):

            num1, num2 = firstList[left]
            num3, num4 = secondList[right]

            max_ = max(max_, max(num2, num4))
            start = max(num1, num3)
            if num2 <= num4:
                end = min(num2, max_)
                if start <= end:
                    result.append([start, end])
                left += 1
            else:
                end = min(num4, max_)

                if start <= end:
                    result.append([start, end])
                right += 1    
                        
        return result    









        