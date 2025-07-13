func isPalindrome(x int) bool {

    if x < 0 {
        return false
    }

    var builder strings.Builder
    num := strconv.Itoa(x)
    runes := []rune (num)
    for i := len(runes) - 1; i >= 0; i-- {
        builder.WriteString(string(runes[i]))
    }

    res := builder.String()
   return res == num
}