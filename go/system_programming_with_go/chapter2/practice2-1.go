package main

import (
    "os"
    "fmt"
)

func main() {
    file, err := os.Create("practice2-1.txt")
    if err != nil {
        panic(err)
    }
    fmt.Fprintf(file, "数値:%d 文字列:%s 浮動小数点数:%f\n", 10, "moji", 3.14)
}
