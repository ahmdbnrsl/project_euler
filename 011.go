package main 

import "fmt"

func squence(idc int64) int64 {
    var current int64 = idc
    var lenSquences int64 = 1
    
    for current != 1 {
        if current % 2 == 0 {
            current /= 2
        } else {
            current = 3*current + 1
        }
        lenSquences += 1
    }
    
    return lenSquences
}

func main() {
    var maximal int64 = 0
    var number int64 = 0
    
    for i := int64(1); i <= int64(1e6); i++ {
        res := squence(i)
        if res > maximal {
            maximal = res
            number = i
        }
    }
    
    fmt.Println(maximal, number)
}