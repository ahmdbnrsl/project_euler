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

func generateDictPrime() {
    var result int64
    
    var i int64 = 0
    var currentNumber int64 = 2
    
    for currentNumber <= int64(4e16) / currentNumber {
        currentNumber += 1
        isPrime := checkPrime(currentNumber)
        
        for !isPrime {
            currentNumber += 1
            isPrime = checkPrime(currentNumber)
        }
        
        if currentNumber < 2e6 {
            result += int64(currentNumber)
        } else {
            break
        }
        
        i++
    }
    
    fmt.Println(result)
}

func main() {
    generateDictPrime()
}