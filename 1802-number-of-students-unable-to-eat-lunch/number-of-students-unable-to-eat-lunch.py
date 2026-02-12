class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = Counter(students)
        queue = deque(students)
        sandwiches = sandwiches[::-1]
        while queue and sandwiches:
            if not count[sandwiches[-1]]:
                break

            popped = queue.popleft()
            if popped == sandwiches[-1]:
                sandwiches.pop()
                count[popped] -= 1
            else:
                queue.append(popped)

        return len(queue)

            
        