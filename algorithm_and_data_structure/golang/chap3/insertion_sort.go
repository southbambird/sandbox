package main

import (
    "fmt"
)

func main() {
    var (
        n int
        list []int
    )
    fmt.Scan(&n)
    list = make([]int, n)
    for i:=0; i < n; i++ {
        fmt.Scan(&list[i])
    }
    list_print(list)
    insertion_sort(list, n)

}

func insertion_sort(a []int, n int ){
    var v, i, j int
    for i = 1 ; i < n ; i++ {
        v = a[i]
        for j = i-1; j >= 0 && a[j] > v; j-- {
            a[j+1] = a[j]
        }
        a[j+1] = v
        list_print(a)
    }
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
