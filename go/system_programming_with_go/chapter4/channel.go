package main

import (
    "fmt"
    "time"
)

func main() {
    done := make(chan bool)
    go func() {
        fmt.Println("start sub()")
        time.Sleep(3 * time.Second)
        fmt.Println("sub() is finished")
        done <- true
    }()

    <-done
    fmt.Println("all tasks are finished")
}
