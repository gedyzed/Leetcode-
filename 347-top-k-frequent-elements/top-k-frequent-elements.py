class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        buckets = defaultdict(list)
        for key, val in counter.items():
            buckets[val].append(key) 
        
        result  = []
        for i in range(len(nums), 0, -1):
            result.extend(buckets[i])
            if len(result) == k:
                break   

        return result 

    
        