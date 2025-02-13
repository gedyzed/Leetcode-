from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        def countingSort(lst):
            max_, min_ = max(lst), min(lst)
            count_array = [0] * (max_ - min_ + 1)

            for num in lst:
                count_array[num - min_] += 1

            sorted_lst = [] 
            for i, count in enumerate(count_array):
                sorted_lst.extend([i + min_] * count) 

            return sorted_lst    

        seats, students = countingSort(seats), countingSort(students)
        moves = 0

        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves
