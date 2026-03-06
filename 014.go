package main 

import "fmt"

func countSundays(startDay, start, end int) int {
    var counter int = 0
    var months []int = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
    for i := start; i<= end; i++ {
        var kabisat bool = (i % 100 == 0 && i % 400 == 0) || (i % 4 == 0 && i % 100 != 0)
        for j, e := range months {
            if startDay % 7 == 0 || startDay == 0 {
                counter += 1
            }
            if j == 1 && kabisat {
                startDay += 29 % 7
            } else {
                startDay += e % 7
            }
        }
    }
    
    return counter
}

func main() {
    sundays := countSundays(2, 1901, 2000)
    fmt.Println(sundays)
}