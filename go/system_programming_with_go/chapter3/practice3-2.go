package main

import (
    "crypto/rand"
    "io"
    "os"
)

func main() {
    file, err := os.Create("practice3-2.txt")
    if err != nil {
        panic(err)
    }
    defer file.Close()
    io.CopyN(file, rand.Reader, 4096)
}
    
