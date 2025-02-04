class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        counter = dict(sorted(counter.items(), key=lambda item : item[1], reverse=True))
        return list(counter.keys())[:k]
        