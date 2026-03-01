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
    
    for currentNumber <= int64(5e12) / currentNumber {
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

func countPositiveDivisors(dictPrime []int64, number int64) int{
    
    var (
        currentIdxPrime int = 0
        powerOfFactor []int
        currentIdxFactor int = 0
        prevIdx int = -1
        prime int64 = dictPrime[currentIdxPrime]
        result int = 1
    )
    
    for number > 1 {
        mod := number % prime == 0
        if mod {
            if currentIdxFactor != prevIdx {
                powerOfFactor = append(powerOfFactor, 1)
                prevIdx += 1
            } else {
                powerOfFactor[prevIdx] += 1
            }
            
            number /= prime
        } else {
            currentIdxPrime += 1
            currentIdxFactor += 1
            
            prime = dictPrime[currentIdxPrime]
        }
    }
    
    for _, e := range powerOfFactor {
        result *= e + 1
    }
    
    return result
}

func firstPositiveDivisorOver500(dictPrime []int64) int64 {
    var start int64 = 1
    var squence int64 = 1
    cpd := 0
    
    
    for cpd <= 500 {
        start += 1
        squence += start
        cpd = countPositiveDivisors(dictPrime, squence)
    }
    
    return squence
}

func main() {
    dictPrime := generateDictPrime()
    FPDO500 := firstPositiveDivisorOver500(dictPrime)
    
    fmt.Println(FPDO500)
}