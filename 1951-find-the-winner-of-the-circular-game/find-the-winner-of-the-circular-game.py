class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue = deque(range(1, n + 1))
        count = 0
        while len(queue) > 1:
            count += 1
            num = queue.popleft()
            if count == k:
                count = 0
                continue

            queue.append(num)

        return queue[0]           