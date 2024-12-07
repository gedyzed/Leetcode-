class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        def countingSort(nums):
            max_, min_ = max(nums), min(nums)
            count = [0] * (max_ - min_ + 1)

            for num in nums:
                count[num - min_] += 1

            sorted_nums = [] 
            for i, freq in enumerate(count):
                sorted_nums.extend([i + min_] * freq)     

            return sorted_nums    

        count = Counter(nums)
        nums_ = list(set(nums))
        min_elements = defaultdict(int)
        nums_ = countingSort(nums_)
        min_elements[nums_[0]] = count[nums_[0]]

        for i in range(1,len(nums_)):
            min_elements[nums_[i]] += count[nums_[i]] + min_elements[nums_[i - 1]]

        answer = []  
        for num in nums:
            answer.append(min_elements[num] - count[num])  

        return answer         