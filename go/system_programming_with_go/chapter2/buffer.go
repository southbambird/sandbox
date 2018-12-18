package main

import (
    "bytes"
    "fmt"
)

func main() {
    var buffer bytes.Buffer
    buffer.Write([]byte("bytes.Buffer example\n"))
    buffer.Write([]byte("2gyoume\n"))
    fmt.Print(buffer.String())
}
