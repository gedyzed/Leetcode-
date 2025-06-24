class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        max_heap, ans = [], 0
        for i in range(1, len(heights)):

            diff = heights[i] - heights[i - 1]
            if not ladders and bricks < diff:
                break

            if diff > 0:
                heappush(max_heap, -diff)
                bricks -= diff

            if bricks < 0: 
                diff = -heappop(max_heap)
                bricks += diff
                ladders -= 1

            ans = i 

        return ans       

                    