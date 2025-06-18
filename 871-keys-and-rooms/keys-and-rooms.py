class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        rooms_entered = 1
        queue = deque([0])
        visited = set([0])
        while queue:

            for _ in range(len(queue)):
                room = queue.popleft()
                for key in rooms[room]:
                    if key not in visited:
                        visited.add(key)
                        queue.append(key)
                        rooms_entered += 1
                    
        return rooms_entered == len(rooms)                





        