package main 

import "fmt"

func checkPrime(number int64) bool{
    var i int64 = 2
    for i <= number/i {
        if number % i == 0 {
            return false
        }
        i++
    }
    return true
}

func generateDictPrime()[]int64 {
    var result []int64 = []int64{2}
    
    var i int64 = 0
    var currentNumber int64 = 2
    
    for currentNumber <= int64(1e11) / currentNumber {
        currentNumber += 1
        isPrime := checkPrime(currentNumber)
        for !isPrime {
            currentNumber += 1
            isPrime = checkPrime(currentNumber)
        }
        
        result = append(result, int64(currentNumber))
        i++
    }
    
    return result
}

func main() {
    dictPrime := generateDictPrime()
    fmt.Println(dictPrime[10000])
}