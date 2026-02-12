class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        queue = deque([(t, i) for i, t in enumerate(tickets)])
        sec = 0
        while queue:
            t, i = queue.popleft()
            sec += 1
            t -= 1
            if i == k and not t:
                return sec

            if t:
                queue.append((t, i))
        
        return sec
        