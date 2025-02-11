class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = left = 0
        right = len(people) - 1
        people.sort()

        while left <= right:

            cur = people[right] + people[left]
            if people[right] == limit or cur > limit:
                boats += 1
            else:  
                boats += 1   
                left += 1

            right -= 1  

        return boats    

  