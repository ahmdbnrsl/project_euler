package main 

import "fmt"
import "math"

func getPerfectOddSquare(num int64) int64 {
    root := int64(math.Sqrt(float64(num)))
    var total int64 = 0
    var i int64 = 1
    for i <= root {
        if i % 2 != 0 {
            total += i * i
        }
        i++
    }
    return total
}

func main() {
    oddSquare := getPerfectOddSquare(279000)
    fmt.Println(oddSquare)
}