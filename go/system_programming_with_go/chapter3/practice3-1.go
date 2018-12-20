package main

import (
    "os"
    "io"
)

func main() {
    oldFile, err := os.Open("old.txt")
    if err != nil {
        panic(err)
    }
    defer oldFile.Close()

    newFile, err := os.Create("new.txt")
    if err != nil {
        panic(err)
    }
    defer newFile.Close()

    io.Copy(newFile, oldFile)
}
    
