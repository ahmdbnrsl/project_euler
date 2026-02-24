package main 

import "fmt"
import "math"

func isPrime(num int64) bool {
    var i int64 = 2
    for i <= int64(math.Sqrt(float64(num))) {
        if num % i == 0 {
            return false
        }
        i++
    }
    return true
}

func generatePrimeAfter(num int64) int64 {
    var prime bool = false
    for !prime {
        num += 1
        prime = isPrime(num)
    }
    return num
}

func largestPrimeFactor(num int64) int64 {
    var prime int64 = 2
    
    for !isPrime(num) {
        for num % prime != 0 {
            prime = generatePrimeAfter(prime)
        }
        
        num = int64(num / prime)
    }
    
    return num
}

func main() {
    number := int64(600851475143)
    largest := largestPrimeFactor(number)
    fmt.Println(largest)
}