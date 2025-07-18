func fib(n int) int {
    if n == 1 {
        return n
    } 
    if n == 0 {
        return 0
    }

    return fib(n - 1) + fib(n - 2)    
}