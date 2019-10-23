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
    for i:=0; i<n; i++ {
        fmt.Scan(&list[i])
    }
    count = selection_sort(list, n)
    list_print(list)
    fmt.Println(count)
}

func selection_sort(a []int, n int) (count int){
    var minj int
    for i, _ := range a {
        minj = i
        for j:=i; j<n; j++ {
            if a[j] < a[minj] {
                minj = j
            }
        }
        a[i], a[minj] = a[minj], a[i]
        if(minj != i) {
            count++
        }
    }
    return
}

func list_print(list []int) {
    for i, val := range list {
        if i == 0 {
            fmt.Print(val)
        } else {
            fmt.Print(" ", val)
        }
    }
    fmt.Println()
}
