package main

import (
    "fmt"
)

type MyError struct {
    Message string
    ErrCode int
}

func (e *MyError) Error() string {
    return e.Message
}

func RaiseError() error {
    return &MyError{Message: "エラーが発生しました", ErrCode: 999}
}

func main() {
    err := RaiseError()
    e, ok := err.(*MyError)
    if ok {
        fmt.Println(e.ErrCode)
    }
}
