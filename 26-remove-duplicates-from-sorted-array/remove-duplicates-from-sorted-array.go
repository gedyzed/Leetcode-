func removeDuplicates(nums []int) int {

    left := 0
    for right := range nums{
        if nums[right] != nums[left]  {
            nums[left + 1] = nums[right]
            left++
        }
    }

    return left + 1
}