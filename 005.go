package main 

import "fmt"

func main() {
    // sum square
    sum := (100 * (100 + 1))/2
    sumSquare := sum * sum
    // sum of square
    sumOfSquare := (100*(100+1)*(2*(100+1)-1))/6
    fmt.Println(sumSquare - sumOfSquare)
}