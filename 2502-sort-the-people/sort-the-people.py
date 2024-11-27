class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_to_names = {}
        for i in range(len(heights)):
            heights_to_names[heights[i]] = names[i]
        max_h = max(heights)
        min_h = min(heights)

        ans = [0] * (max_h - min_h + 1)
        for height in heights :
            ans[height - min_h] += 1

        answer = []   
        for i in range(len(ans)- 1, -1 ,-1):
            if ans[i]:
                answer.append(i + min_h)
        
        for i, ans in enumerate(answer) :
            names[i] = heights_to_names[ans] 

        return names  