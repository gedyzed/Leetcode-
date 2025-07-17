import "strconv"

func reverse(x int) int {

    str := []rune(strconv.Itoa(x))
    ans := strings.Builder{}
    if x < 0 {
        ans.WriteString("-")
    }
    for i := len(str) - 1; i >= 0; i-- {
        if str[i] == '-'{
            continue
        }
        ans.WriteString(string(str[i]))
    } 
    res := ans.String()
    answer, _ := strconv.Atoi(res) 

    const INT_MIN = -2147483648 // -2^31
    const INT_MAX = 2147483647  // 2^31 - 1
    if answer < INT_MIN || answer > INT_MAX {
        return 0
    }

    return answer
}