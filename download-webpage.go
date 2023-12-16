package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func download(url string) {
	resp, err := http.Get(url)
	defer resp.Body.Close()

	if err != nil {
		fmt.Println(err)
	}

	bodyBytes, err := io.ReadAll(resp.Body) // parse for bytes
	if err != nil {
		fmt.Println(err)
	}

	bodyString := string(bodyBytes)
	fmt.Println(bodyString)
}

func main() {
	url := os.Args[1]
	download(url)
}
