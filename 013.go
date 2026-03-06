package main 

import "fmt"

func toSpell(number int, tipe string) string {
    var (
        units []string = []string{
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        }
        dozens []string = []string{
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen",
        }
        teens []string = []string{
            "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
        }
    )
    
    switch tipe {
    case "units":
        return units[number - 1]
    case "dozens":
        return dozens[number - 1]
    case "teens":
        return teens[number - 2]
    case "hundreds":
        return units[number - 1] + "hundred"
    case "thousands":
        return units[number - 1] + "thousand"
    default:
        return ""
    }
}
    
func iterateAndCount() string {
    x := 1546
    thousand_mod := x % 1000 // 546
    hundred_mod := x % 100 // 46
    ten_mod := x % 10 // 6
    
    str := ""
    
    
    
    
}

func main() {
    fmt.Println(something())
}