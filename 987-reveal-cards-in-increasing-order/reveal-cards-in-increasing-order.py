class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque (range(n))
        answer = [0] * n
        deck.sort()

        for i in range(n):
            answer[queue.popleft()] = deck[i]
            if len(queue) > 1:
                queue.append(queue.popleft())
               
        return answer    

        
        