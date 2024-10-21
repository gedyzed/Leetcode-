class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        cards_to_count = defaultdict(int)
        min_length = 1000000 #since the max card[i] = 10^6
        left = 0
        
        for right in range(len(cards)):
            cards_to_count[cards[right]] += 1
            while cards_to_count[cards[right]] > 1:
                min_length = min(min_length, right - left + 1)
                cards_to_count[cards[left]] -= 1
                left += 1

        return min_length if min_length != 1000000 else -1             




        