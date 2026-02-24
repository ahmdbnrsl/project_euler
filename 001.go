package main 

import "fmt"

func fibonacci() {
    var (
        result int64 = 0
        prev int64 = 0
        now int64 = 1
    )
    
    for now <= 4e6 {
        o := prev + now
        prev = now
        now = o
        
        if now % 2 == 0 {
            result += now
        }
    }
    fmt.Println(now)
    fmt.Println(result)
}

func main() {
    fibonacci()
}