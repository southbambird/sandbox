package main

import (
    "io"
    "os"
)

func main() {
    input_file, err := os.Open("file.go")
    if err != nil {
        panic(err)
    }
    defer input_file.Close()

    output_file, err := os.Create("copy_file.txt")
    if err != nil {
        panic(err)
    }
    defer output_file.Close()

    io.Copy(output_file, input_file)
}
