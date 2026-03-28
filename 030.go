package main 

import (
    "fmt"
    "strconv"
    "math"
)

func getProdNthDigit(request []int) int {
    currentDigit := 9
    packDigit := 1
    
    prevDigit := 0
    prevRequest := 0
    
    prod := 1
    for _, e := range request {
        for e > currentDigit {
            prevDigit = currentDigit
            packDigit += 1
            currentDigit += 9 * int(math.Pow(10, float64(packDigit - 1))) * packDigit
        }
        
        index := e - prevDigit
        
        var divide int
        var modulo int
        
        if index < packDigit {
            divide = int(e / index) - index
            modulo = e % divide
        } else {
            divide = int(index / packDigit)
            modulo = index % packDigit
        }
        
        number := divide + prevRequest
        if e <= 1 {
            modulo += 1
        }

        digit := string(strconv.Itoa(number)[modulo - 1])
        digitNumber, _ := strconv.Atoi(digit)
        prod *= digitNumber
        prevRequest = e
    }
    
    return prod
}

func main() {
    request := []int{1, 10, 100, 1000, 10000, 100000, 1000000, 10000000}
    
    gpnd := getProdNthDigit(request)
    fmt.Println(gpnd)
}