class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums_ = sorted(nums)
        count = {}
        result = []

        for i in range(len(nums_)):
            if nums_[i] not in count:
                count[nums_[i]] = i
        for i in range(len(nums)):
            result.append(count[nums[i]])    

        return result        






        count = Counter(nums)

        nums_ = list(set(nums))
        nums_.sort()
        min_elements = defaultdict(int)
        min_elements[nums_[0]] = count[nums_[0]]

        for i in range(1,len(nums_)):
            min_elements[nums_[i]] += count[nums_[i]] + min_elements[nums_[i - 1]]

        answer = []  
        for num in nums:
            answer.append(min_elements[num] - count[num])  

        return answer         