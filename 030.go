package main 

import (
    "fmt"
    "strconv"
    "math"
)

func getProdNthDigit(request []int) int {
    capacityDigit := 9
    packDigit := 1
    
    prevDigit := 0
    //prevRequest := 0
    
    prevNumber := 0
    
    prod := 1
    for _, e := range request {
        for e > capacityDigit {
            prevNumber += 9 * int(math.Pow(10, float64(packDigit - 1)))
            prevDigit = capacityDigit
            packDigit += 1
            capacityDigit += 9 * int(math.Pow(10, float64(packDigit - 1))) * packDigit
        }
        
        number := prevNumber + int(math.Ceil(float64((e - prevDigit) / packDigit)))
        digit := strconv.Itoa(number)
        
        
        fmt.Println(string(digit), e % packDigit - (packDigit % 2))

        // digit := string(strconv.Itoa(number)[modulo - 1])
        // digitNumber, _ := strconv.Atoi(digit)
        prod *= 1
        //prevRequest = e
    }
    
    return prod
}

func main() {
    request := []int{4, 16, 127, 211, 216, 320, 610}
    
    gpnd := getProdNthDigit(request)
    fmt.Println(gpnd)
}