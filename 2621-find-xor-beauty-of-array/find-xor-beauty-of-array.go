func xorBeauty(nums []int) int {

    x := 0
    for _, num := range nums {
        x ^= num
    }

    return x
    
}