class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        queries.sort(key=lambda x: x[0])
        heap = []
        diff_array = [0] * (len(nums) + 1)
        operations = j = 0

        for i, num in enumerate(nums):
            operations += diff_array[i]

            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1

            while operations < num and heap and -heap[0] >= i:
                operations += 1
                diff_array[-heappop(heap) + 1] -= 1

            if operations < num:
                return -1

        return len(heap)        

                   