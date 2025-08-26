class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        max_dg = ans = 1
        for nums in dimensions:
            l, w = nums
            sqrt = math.sqrt(l * l + w * w)
            if max_dg < sqrt:
                max_dg = sqrt
                ans = l * w

            if max_dg == sqrt:
                ans = max(ans, l * w)

        return ans            

        