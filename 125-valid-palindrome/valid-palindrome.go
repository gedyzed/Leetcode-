func isPalindrome(s string) bool {

    lower := strings.ToLower(s)
    var builder strings.Builder
    for _, r := range lower {
        if unicode.IsLetter(r) || unicode.IsDigit(r) {
            builder.WriteString(string(r))
        }
    } 

    s = builder.String()
    var reverse strings.Builder
    rev := [] rune(s)
    for i := len(rev) - 1; i >= 0; i-- {
        reverse.WriteString(string(rev[i])) 
    }

    return s ==  reverse.String()  



    
    
}