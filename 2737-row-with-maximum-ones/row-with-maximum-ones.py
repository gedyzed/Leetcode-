class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        row = max_sum = 0
        for i, rows in enumerate(mat):
            sum_ = sum(rows)
            if sum_ > max_sum:
                max_sum = sum_
                row = i

        return [row, max_sum]            

        