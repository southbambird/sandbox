package main

import (
    "fmt"
)

func main() {
    var (
        n, count int
        list []int
    )
    fmt.Scan(&n)
    list = make([]int, n)
    for i:=0; i < n; i++ {
        fmt.Scan(&list[i])
    }
    count = bubble_sort(list, n)
    list_print(list)
    fmt.Println(count)
    
}

func bubble_sort(a []int, n int) (count int){
    var (
        flag bool = true
    )
    count = 0
    for flag {
        flag = false
        for i := n - 1 ; i > 0 ; i-- {
            if a[i] < a[i-1] {
                a[i], a[i-1] = a[i-1], a[i]
                flag = true
                count++
            }
        }
    }
    return 
}

func list_print(list []int) {
    var i int
    for i=0; i<len(list); i++ {
        if i == 0 {
            fmt.Print(list[i])
        } else {
            fmt.Print(" ", list[i])
        }
    }
    fmt.Print("\n")
}
