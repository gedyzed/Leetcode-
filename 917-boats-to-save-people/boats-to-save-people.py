class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = left = 0
        right = len(people) - 1
        people.sort()

        while left <= right:

            if people[right] + people[left] <= limit:
                left += 1
            boats += 1
            right -= 1  

        return boats    

  