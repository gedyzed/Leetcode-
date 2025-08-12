class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def num_to_pos(num):
            r = n - 1 - (num - 1) // n
            c = (num - 1) % n
            if ((n - 1 - r) % 2 == 1): 
                c = n - 1 - c
            return r, c
       
        n = len(board)
        queue = deque([1])
        visited = set([1])
        moves = 0
        while queue:

            for _ in range(len(queue)):
                curr = queue.popleft()
                min_ = min(curr + 6, n * n)
                if curr == n * n:
                    return moves

                for next in range(curr + 1, min_ + 1):
                    row, col = num_to_pos(next)
                    if board[row][col] != -1:
                        next = board[row][col]

                    if next not in visited:
                        queue.append(next) 
                        visited.add(next)

            moves += 1        
        
        return -1        
            



    
                  

        
        