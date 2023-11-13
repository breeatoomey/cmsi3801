package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	n, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Println("requires int arg")
		fmt.Printf("got %s\n", err)
	} else {
		for i := 1; i <= n; i++ {
			fmt.Println(i * i)
		}
	}
}
