func twoSum(nums []int, target int) []int {

    dict := make(map[int]int)
    x := 0
    for i, num := range nums {
        x = target - num
        _, ok := dict[x]
        if ok {
            return []int{dict[x], i}
        }
        dict[num] = i
    } 
    return []int{}
}