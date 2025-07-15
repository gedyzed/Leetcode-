func majorityElement(nums []int) int {

    counter := make(map[int]int)
    n := len(nums) / 2.0 
    for _, num := range nums {
        counter[num]++
        if counter[num] > n {
            return num
        }
    }

    return -1
  
}