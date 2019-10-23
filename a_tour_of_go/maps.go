package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	var counter = make(map[string]int)
	words := strings.Fields(s)
	for _, word := range words {
		_, ok := counter[word]
		if ok {
			counter[word]++
		}else {
			counter[word] = 1
		}
	}
	return counter
}

func main() {
	wc.Test(WordCount)
}
