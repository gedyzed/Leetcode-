class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        queue = deque(range(len(deck)))
        result = [0] * len(deck)

        for i in range(len(deck)):
            result[queue.popleft()] = deck[i] 
            if queue:
                queue.append(queue.popleft())
   
        return result        

        