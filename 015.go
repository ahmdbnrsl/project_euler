package main

import "fmt"
import "math"
import "slices"

func getSumPositiveDivisor(number int64) int64 {
	var results int64 = 0
	for i := int64(1); i <= int64(math.Sqrt(float64(number))); i++ {
		if number % i == 0 {
    		if i == int64(number / i) {
        		results += i
    		} else {
        		results += int64(number / i) + i
    		}
		}
	}
	return results - number
}

func checkAbundant(number int64) bool {
	return getSumPositiveDivisor(number) > number
}

func main() {
	var limit int64 = 28123
	var currentSum int64 = 0
	var sumOfTwoAbundantNumbers []int64

	for i := int64(12); i <= limit; i++ {
		if currentSum > limit {
			break
		}
		if checkAbundant(i) {
			for j := i; j <= limit; j++ {
				if checkAbundant(j) {
					if i + j <= limit {
						currentSum = i + j
						if !slices.Contains(sumOfTwoAbundantNumbers, currentSum) {
							sumOfTwoAbundantNumbers = append(sumOfTwoAbundantNumbers, currentSum)
						}
					}
				}
			}
		}
	}

	var notSumOfTwoAbundantNumbers int64 = 0

	for i := int64(1); i <= 28123; i++ {
		
		if !slices.Contains(sumOfTwoAbundantNumbers, i) {
			notSumOfTwoAbundantNumbers += i
		}
	}

	fmt.Println(notSumOfTwoAbundantNumbers)
}