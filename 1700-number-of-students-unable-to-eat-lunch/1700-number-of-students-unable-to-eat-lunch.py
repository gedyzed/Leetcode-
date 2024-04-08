class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        numberOfStudents = 0

        while True:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0)) 
            if not len(sandwiches) :
                break
            elif sandwiches[0] not in students:
                numberOfStudents = len(students)
                break
        return numberOfStudents  

    